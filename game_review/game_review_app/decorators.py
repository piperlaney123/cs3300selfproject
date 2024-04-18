from django.http import HttpResponse
from .models import *

def must_own_review(func):
    def wrapper_func(request, *args, **kwargs):
        pk = kwargs["review_id"]
        review = Review.objects.get(pk=pk)
        if not (review.reviewuser.user.id == request.user.id):
            return HttpResponse("You are not authorized to view this page")
        return func(request, *args, **kwargs)
    return wrapper_func

def must_own_userprofile(func):
    def wrapper_func(request, *args, **kwargs):
        pk = kwargs["user_id"]
        reviewuser = ReviewUser.objects.get(pk=pk)
        if not (reviewuser.user.id == request.user.id):
            return HttpResponse("You are not authorized to view this page")
        return func(request, *args, **kwargs)
    return wrapper_func


# review = Review.objects.get(pk=review_id) reviewuser = ReviewUser.objects.get(pk=user_id)
# reviewuser = ReviewUser.objects.get(pk=user_id)
