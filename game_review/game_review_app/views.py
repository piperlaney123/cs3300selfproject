from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
from taggit.models import Tag
from .forms import ReviewForm, UserForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from .decorators import must_own_review, must_own_userprofile
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
#from django.http import HttpResponse


def index(request):
   game_reviews = Review.objects.all()
    # Render the HTML template index.html with the data in the context variable.
   return render( request, 'game_review_app/index.html', {'game_reviews':game_reviews})
    
    
def ReviewDetailView(request, review_id):
    review = Review.objects.get(pk=review_id)
    # this is my object-level permission check
    # isOwner tests if the authenticated user (request.user.id) matches the review's user
    # (note: this is a bit derivative as I created my own user class, that renamed to reviewuser, so I could
    # create a one-to-one relationship with Djanog's built in user class. thus, reviewuser is tied to user, so 
    # i test request.user.id with review.reviewuser.user_id -- does that makes sense? in the end its testing the 
    # authenticated user's id.)
    isOwner = request.user.id == review.reviewuser.user_id
    isAuthenticated = request.user.is_authenticated
    
    return render(request, 'game_review_app/review_detail.html', {'review':review, 'isOwner':isOwner, 'isAuthenticated': isAuthenticated })


# OKAY BRO. U USED THE VARIABLE NAME 'user' THAT WAS FUCKING UP user.is_authenticated IN BASE TEMPLATE
# THATS WHY THE LOGIN WASNT WORKING ON THESE SPECIFIC PAGES. YOU CHANGED user TO reviewuser AND 
# IT FIXED THIS PROBLEM. YOU MAY WANT TO LOOK AT OTHER VIEW FUNCS TO MAKE SURE THIS PROBLEM DOESNT PERSIST.
def UserDetailView(request, user_id):
    reviewuser = ReviewUser.objects.get(pk=user_id)
    reviews = Review.objects.filter(reviewuser_id=user_id)
    isOwner = request.user.id == reviewuser.user_id
    isAuthenticated = request.user.is_authenticated
    return render(request, 'game_review_app/user_detail.html', {'reviewuser':reviewuser, 'reviews':reviews, 'isOwner': isOwner, 'isAuthenticated': isAuthenticated})


@login_required(login_url='login') 
@must_own_userprofile
def createReview(request, user_id):
    form = ReviewForm()

    user = ReviewUser.objects.get(pk=user_id)

    if request.method == 'POST':
        review_data = request.POST.copy()
        review_data['user_id'] = user_id
        form = ReviewForm(review_data)
        if form.is_valid:
            review = form.save(commit=False)
            review.reviewuser = user
            review.save()
            # come back to this line of code, for some reason it saves the form's tags; without it, tag arent saved. 
            form.save_m2m()

            return redirect('user-detail', user_id)
        
    context = {'form': form}
    return render(request, 'game_review_app/review_form.html', context)


@login_required(login_url='login') 
@must_own_review
def updateReview(request, user_id, review_id):
    # get review according to id so update can work
    review = Review.objects.get(pk=review_id)
    # get form with data from review
    form = ReviewForm(instance = review)
    reviewuser = ReviewUser.objects.get(pk=user_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid:
            form.save()
            #form.save_m2m()
            reviewuser.review = review

            return redirect('review-detail', review_id)
        
    context = {'form': form}
    return render(request, 'game_review_app/review_form.html', context)

@login_required(login_url='login') 
@must_own_review
def deleteReview(request, user_id, review_id):
    review = Review.objects.get(pk=review_id)

    if request.method == 'POST':
        review.delete()
        return redirect('user-detail', user_id)
    
    context = {'review': review}
    return render(request, 'game_review_app/delete_review.html', context)

class ReviewUserListView(generic.ListView):
    model = ReviewUser


@login_required(login_url='login') 
@must_own_userprofile
def updateUser(request, user_id):
    reviewuser = ReviewUser.objects.get(pk=user_id)
    form = UserForm(instance = reviewuser)

    if request.method == "POST":
        form = UserForm(request.POST, instance = reviewuser)
        if form.is_valid:
            form.save()

            return redirect('user-detail', user_id)
        
    context = {'form': form}
    return render(request, 'game_review_app/user_form.html', context)


def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user_role')
            user.groups.add(group)
            reviewuser = ReviewUser.objects.create(user=user,)
            reviewuser.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        
    context = {'form': form}
    return render(request, 'registration/register.html', context)

# makes it so you cant just enter the url as unlogged in user to get to this page
# must be logged in user to gett to user page
@login_required(login_url='login') 
def userPage(request):
    reviewuser = request.user.reviewuser
    reviews = Review.objects.filter(reviewuser_id=reviewuser.id)
    form = UserForm(instance = reviewuser)
    print('user', reviewuser)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance = reviewuser)
        if form.is_valid():
            form.save()
            
            

    context = {'form':form, 'reviewuser': reviewuser, 'reviews':reviews}
    return render(request, 'game_review_app/user.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

class SearchResultsView(ListView):
    model = Review
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Review.objects.filter(Q(game_title__icontains=query) | Q(tags__name__in=[query]))
        return object_list
    

'''
def index(request):
   game_reviews = Review.objects.all()
    # Render the HTML template index.html with the data in the context variable.
   return render( request, 'game_review_app/index.html', {'game_reviews':game_reviews})
'''