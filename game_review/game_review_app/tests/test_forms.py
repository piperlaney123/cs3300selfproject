from django.test import TestCase
from game_review_app.forms import *
from django.contrib.auth.models import User

class ReviewFormTestCase(TestCase):

    def test_valid_form(self):
        data = {'game_title': 'Game Title', 'tags': 'tag1', 'review_summary': 'review summary', 'would_recommend': 'Yes','rating': 4}
        form = ReviewForm(data=data)
        self.assertTrue(form.is_valid())

    def test_missing_attributes_invalid(self):
        # test field validation -- all fields but summary are required
        data = {'game_title': '', 'tags': '', 'review_summary': '', 'would_recommend': '','rating': ''}
        form = ReviewForm(data=data)
        self.assertFalse(form.is_valid()) and self.assertIn('game_title', form.errors, 'tags', form.errors, 'would_recommend', form.errors, 'rating', form.errors)

class ReviewUserFormTestCase(TestCase):

    def test_valid_form(self):
        data = {'name': 'Test User', 'about': "Test about", 'is_active_user': True, 'preferred_game_genres': 'genre'}
        form = UserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_missing_attributes_invalid(self):
        # test field validation -- all fields but about are required
        data = {'name': '', 'about': "", 'is_active_user': '', 'preferred_game_genres': ''}
        form = UserForm(data=data)
        self.assertFalse(form.is_valid()) and self.assertIn('name', form.errors, 'is_active_user', form.errors, 'preferred_game_genres', form.errors)

