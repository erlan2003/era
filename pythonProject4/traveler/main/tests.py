from django.test import TestCase

from django.test import TestCase
from django.urls import reverse

class TestAttraction(TestCase):

    def test_index(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_tours(self):
        response = self.client.get(reverse('tours'))
        self.assertEqual(response.status_code, 200)

    def test_add_attraction(self):
        response = self.client.get(reverse('add_attraction'))
        self.assertEqual(response.status_code, 200)