from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.

class ReviewUser(models.Model):

    name = models.CharField(max_length=200)
    about = models.TextField(blank = True)
    is_active_user = models.BooleanField(default = False)
    preferred_game_genres = TaggableManager()
    # for authentication 
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("user-detail", args=[str(self.id)])

class Review(models.Model):

    game_title = models.CharField(max_length=200)
    # List of choices for major in database, human readable name
  
    tags = TaggableManager()
    review_summary = models.TextField(blank = True)
    reviewuser = models.ForeignKey(ReviewUser, on_delete=models.CASCADE)
    OPTIONS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    would_recommend = models.CharField(max_length=200, choices=OPTIONS)
    rating = models.PositiveIntegerField(default=0, choices=((i,i) for i in range(0,6)))

    def __str__(self):
        return self.game_title
    
    def get_absolute_url(self):
        return reverse("review-detail", args=[str(self.id)])
    
