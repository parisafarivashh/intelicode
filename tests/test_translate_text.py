import pytest

from django.urls import reverse
from rest_framework.test import APITransactionTestCase

from authorize.models import User


class TranslateViewTest(APITransactionTestCase):

    @classmethod
    @pytest.mark.django_db
    def setUp(cls):
        cls.user = User.objects.create_user(
            title='user1',
            email='user1@gmail.com',
            password='password',
        )

    def login(self):
        response = self.client.post(
            reverse('login'),
            data=dict(email=self.user.email, password='password'),
        )
        token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_translate_text(self):
        self.login()
        data = {
            'body': 'hi, how are you?',
            'translate_to': 'spanish',
        }
        response = self.client.post(reverse('translate'), data)
        assert response.json() == {'result': 'Hola, ¿cómo estás?'}

