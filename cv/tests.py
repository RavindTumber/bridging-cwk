from django.test import TestCase
from django.urls import resolve
from cv.views import display_cv

class CVPageTest(TestCase):

    def test_root_url_resolves_to_cv_page_view(self):
        found = resolve('/cv/')  
        self.assertEqual(found.func, display_cv)
