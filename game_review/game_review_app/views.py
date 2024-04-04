from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
from taggit.models import Tag
from .forms import ReviewForm

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

            return redirect('user-detail', user_id)
        
    context = {'form': form}
    return render(request, 'game_review_app/review_form.html', context)


