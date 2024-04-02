from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):


# Render the HTML template index.html with the data in the context variable.
   return render( request, 'game_review_app/index.html')