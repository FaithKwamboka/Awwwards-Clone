from django.test import TestCase
from .models import *
import unittest

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Kwash', password='kwamboka')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Kwash')
        self.post = Post.objects.create(id=1, title='test post', photo='https://ucarecdn.com/44783a4c-9b13-4bbe-852d-259388717c01/', description='desc',
                                        user=self.user, url='http://url.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        self.assertTrue(len(post) < 1)


class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Kwash')
        self.post = Post.objects.create(id=1, title='test post', photo='https://ucarecdn.com/44783a4c-9b13-4bbe-852d-259388717c01/', description='desc',
                                        user=self.user, url='http://url.com')
        self.rating = Rating.objects.create(id=1, design=6, usability=10, content=8, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_post_rating(self, id):
        self.rating.save()
        rating = Rating.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)
        
        
if __name__ == '__main__':
    unittest.main()  

