from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('game_title', 'tags', 'review_summary', 'would_recommend')
