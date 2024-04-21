from django.test import TestCase
from django.contrib.auth.models import User
from game_review_app.models import *

class ModelTestCase(TestCase):
    def setUp(self):
        # create user
        self.user = User.objects.create_user(username='testuser5000', password='shedoBtesting12')

        # create reviewuser
        self.reviewuser = ReviewUser.objects.create(
            name = 'Test User 5000',
            about = 'Test about',
            is_active_user = True,
            preferred_game_genres = 'genre1',
            user = self.user
        )

        # create review
        self.review = Review.objects.create(
            game_title = 'Game1',
            tags = 'tag1',
            review_summary = 'test summary',
            would_recommend = 'Yes',
            rating = 3,
            reviewuser = self.reviewuser
        )

    def test_reviewuser_creation(self):
        # attributes
        self.assertEqual(self.reviewuser.name, 'Test User 5000')
        self.assertEqual(self.reviewuser.about, 'Test about')
        self.assertEqual(self.reviewuser.is_active_user, True)
        self.assertEqual(self.reviewuser.preferred_game_genres, 'genre1')
        self.assertEqual(self.reviewuser.user, self.user)
        # methods
        self.assertEqual(str(self.reviewuser), self.reviewuser.name)
        self.assertEqual(self.reviewuser.get_absolute_url(), '/user/1')

    def test_review_creation(self):
        # attributes
        self.assertEqual(self.review.game_title, 'Game1')
        self.assertEqual(self.review.tags, 'tag1') 
        self.assertEqual(self.review.review_summary, 'test summary')
        self.assertEqual(self.review.would_recommend, 'Yes')
        self.assertEqual(self.review.rating, 3)
        self.assertEqual(self.review.reviewuser, self.reviewuser)
        # methods
        self.assertEqual(str(self.review), self.review.game_title) 
        self.assertEqual(self.review.get_absolute_url(), '/review/1') 
