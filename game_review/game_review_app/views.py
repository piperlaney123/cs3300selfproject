from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
from taggit.models import Tag

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
    rating = Rating.objects.filter(review_id=review_id).first()
    return render(request, 'game_review_app/review_detail.html', {'review':review, 'rating': rating})

class UserDetailView(generic.DetailView):
    model = User

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)



