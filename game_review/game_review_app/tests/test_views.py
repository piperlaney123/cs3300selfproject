from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from game_review_app.models import *

class ViewsTestCase(TestCase):
    def setUp(self):

        self.client = Client()

        # create a test user
        self.user = User.objects.create_user(username="testuser", email='test@gmail.com', password="testingtest123")

        # create a test ReviewUser
        self.reviewuser = ReviewUser.objects.create(
            name="Test User",
            about="Test About",
            is_active_user = True,
            preferred_game_genres = "rpg",
            user = self.user
        )

        
        # create a test review
        self.gamereview = Review.objects.create(
            game_title="Game Title",
            tags = "tag",
            review_summary = "Test Summary",
            reviewuser = self.reviewuser,
            would_recommend = "Yes",
            rating = 4,
        )
        
        self.client.login(username="testuser", password="testingtest123")
        

    def testLogin(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        
    
    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_review_app/index.html')

    def test_user_detail_view(self):
        client = Client()
        response = client.get(reverse('user-detail', kwargs={'user_id': self.reviewuser.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_review_app/user_detail.html')

    
    def test_review_detail_view(self):
        client = Client()
        response = client.get(reverse('review-detail', kwargs={'review_id': self.gamereview.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_review_app/review_detail.html')
    

    def test_create_review_view(self):
        #client = Client() a lot of trouble shooting for login decorator -- logged in as client in set up func, 
        #now this def will use self.client instead
        response = self.client.get(reverse('review-create', kwargs={'user_id': self.reviewuser.id}))
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'game_review_app/review_form.html')

        
        # test POST request
        data = {'game_title': "Test title", 'tags': 'tag1', 'review_summary': 'test summary', 'would_recommend': 'Yes', 'rating': 4}
        response = self.client.post(reverse('review-create', kwargs={'user_id': self.reviewuser.id}), data=data)
        self.assertEqual(response.status_code, 302) # redirect after successful form submission 
      

        # check if review was actually created
        review_count = Review.objects.filter(reviewuser=self.reviewuser).count()
        self.assertEqual(review_count, 2) 

    def test_create_review_view_invalid_form(self):
        response = self.client.get(reverse('review-create', kwargs={'user_id': self.reviewuser.id}), {}) # empty!
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "This field is required")



    

    