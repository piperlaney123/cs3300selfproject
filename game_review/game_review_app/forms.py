from django.forms import ModelForm
from .models import Review, ReviewUser
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('game_title', 'tags', 'review_summary', 'would_recommend','rating')

class UserForm(ModelForm):
    class Meta:
        model = ReviewUser
        fields = ('name', 'about', 'is_active_user', 'preferred_game_genres')
        #fields = '__all__'
        #exclude = ['user']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


