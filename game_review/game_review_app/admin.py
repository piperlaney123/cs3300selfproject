from django.contrib import admin
from .models import ReviewUser
from .models import Review

# Register your models here.
admin.site.register(ReviewUser)
admin.site.register(Review)

