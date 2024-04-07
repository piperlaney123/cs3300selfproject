from django.forms import ModelForm
from .models import Review, User
from django.forms.models import inlineformset_factory


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('game_title', 'tags', 'review_summary', 'would_recommend','rating')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'about', 'is_active_user', 'preferred_game_genres')



