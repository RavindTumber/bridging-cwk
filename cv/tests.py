from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from cv.views import display_cv

class CVPageTest(TestCase):

    def test_root_url_resolves_to_cv_page_view(self):
        found = resolve('/cv/')  
        self.assertEqual(found.func, display_cv)

    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()
        response = display_cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>CV</title>', html)
