from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetup(APITestCase):
    ''' Test setup'''


    def setUp(self) -> None:
        self.registerurl=reverse('user')

        return super().setUp()
    