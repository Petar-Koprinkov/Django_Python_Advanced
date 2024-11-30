from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from forumApp.posts.models import Books

UserModel = get_user_model()


class ApprovePostsTestCase(TestCase):
    def setUp(self):
        self.user_credential = {
            'username': 'pkoprinkov10',
            'email': 'petarkoprinkov@abv.bg',
            'password': '56932957eH10',
        }

        self.user = UserModel.objects.create_user(**self.user_credential)

        self.post = {
            'title': "My book",
            'content': 'Hello',
            'author': self.user,
            'approved': False,
        }

    def test__approved_test__approves_post(self):
        self.client.login(**self.user_credential)
        post = Books.objects.create(**self.post)

        response = self.client.get(
            reverse('approve', args=[post.pk]),
            HTTP_REFERER=reverse('index')
        )

        post.refresh_from_db()
        self.assertTrue(post.approved)
        self.assertRedirects(response, reverse('index'))


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.user_credential = {
            'username': 'pkoprinkov10',
            'email': 'petarkoprinkov@abv.bg',
            'password': '56932957eH10',
        }

        self.user = UserModel.objects.create_user(**self.user_credential)

    def test__return_user_in_the_context(self):
        user = self.client.login(**self.user_credential)
        response = self.client.get(reverse('index'))

        self.assertTrue(user)
