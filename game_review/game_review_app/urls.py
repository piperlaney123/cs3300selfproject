from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('', views.login, name='login'),
path('', views.logout, name='logout'),
#path('review/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
path('review/<int:review_id>', views.ReviewDetailView, name='review-detail'),
] 
