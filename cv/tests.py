from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from cv.views import display_cv

class CVPageTest(TestCase):

    def test_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html')
