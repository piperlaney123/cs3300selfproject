from django.urls import path, include
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
#path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
path('review/<int:review_id>', views.ReviewDetailView, name='review-detail'),
path('user/<int:user_id>', views.UserDetailView, name='user-detail'),
path('user/<int:user_id>/review/create/', views.createReview, name='review-create'),
path('user/<int:user_id>/edit_review/<int:review_id>/', views.updateReview, name='update-review'),
path('user/<int:user_id>/delete_review/<int:review_id>/', views.deleteReview, name='delete-review'),
path('users/', views.ReviewUserListView.as_view(), name='user-list'),
path('user/update/<int:user_id>/', views.updateUser, name='update-user'),
path('accounts/', include('django.contrib.auth.urls')),
path('accounts/register/', views.registerPage, name = 'register_page'),
path('user/', views.userPage, name='user-page'),
#path('login/', views.loginPage, name='login'),
path('logout/', views.logoutUser, name='logout'),

] 
