from django.forms import ModelForm
from .models import Review
from django.forms.models import inlineformset_factory


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('game_title', 'tags', 'review_summary', 'would_recommend','rating')



