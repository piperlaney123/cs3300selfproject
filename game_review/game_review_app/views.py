from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
from taggit.models import Tag
from .forms import ReviewForm, UserForm

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   game_reviews = Review.objects.all()



# Render the HTML template index.html with the data in the context variable.
   return render( request, 'game_review_app/index.html', {'game_reviews':game_reviews})

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')

'''
class ReviewDetailView(generic.DetailView):
    model = Review
    rating = Review.objects.get(pk=model.pk)
'''
    
def ReviewDetailView(request, review_id):
    review = Review.objects.get(pk=review_id)
    #rating = Rating.objects.filter(review_id=review_id).first()
    return render(request, 'game_review_app/review_detail.html', {'review':review})

'''
class UserDetailView(generic.DetailView):
    model = User
'''

def UserDetailView(request, user_id):
    user = User.objects.get(pk=user_id)
    reviews = Review.objects.filter(user_id=user_id)
    return render(request, 'game_review_app/user_detail.html', {'user':user, 'reviews':reviews})


def createReview(request, user_id):
    form = ReviewForm()

    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        review_data = request.POST.copy()
        review_data['user_id'] = user_id
        form = ReviewForm(review_data)
        if form.is_valid:
            review = form.save(commit=False)
            review.user = user
            review.save()
            # come back to this line of code, for some reason it saves the form's tags; without it, tag arent saved. 
            form.save_m2m()

            return redirect('user-detail', user_id)
        
    context = {'form': form}
    return render(request, 'game_review_app/review_form.html', context)


def updateReview(request, user_id, review_id):
    # get review according to id so update can work
    review = Review.objects.get(pk=review_id)
    # get form with data from review
    form = ReviewForm(instance = review)
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid:
            form.save()
            #form.save_m2m()
            user.review = review

            return redirect('review-detail', review_id)
        
    context = {'form': form}
    return render(request, 'game_review_app/review_form.html', context)

def deleteReview(request, user_id, review_id):
    review = Review.objects.get(pk=review_id)

    if request.method == 'POST':
        review.delete()
        return redirect('user-detail', user_id)
    
    context = {'review': review}
    return render(request, 'game_review_app/delete_review.html', context)

class UserListView(generic.ListView):
    model = User


def updateUser(request, user_id):
    user = User.objects.get(pk=user_id)
    form = UserForm(instance = user)

    if request.method == "POST":
        form = UserForm(request.POST, instance = user)
        if form.is_valid:
            form.save()

            return redirect('user-detail', user_id)
        
    context = {'form': form}
    return render(request, 'game_review_app/user_form.html', context)
               

