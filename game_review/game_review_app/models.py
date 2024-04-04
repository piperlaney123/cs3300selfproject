from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=200)
    about = models.TextField(blank = True)
    is_active_user = models.BooleanField(default = False)
    preferred_game_genres = TaggableManager()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("user_detail", args=[str(self.id)])

class Review(models.Model):

    game_title = models.CharField(max_length=200)
    # List of choices for major in database, human readable name
    '''STAR_RATING = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five')
    )

    star_rating = models.CharField(max_length=200, choices=STAR_RATING)'''
    tags = TaggableManager()
    review_summary = models.TextField(blank = True)
    #would_recommend = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    OPTIONS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    would_recommend = models.CharField(max_length=200, choices=OPTIONS)
    rating = models.PositiveIntegerField(default=0, choices=((i,i) for i in range(0,6)))

    def __str__(self):
        return self.game_title
    
    def get_absolute_url(self):
        return reverse("review_detail", args=[str(self.id)])
    
