from django.test import TestCase
from django.contrib.auth.models import User

from .models import Education
from .forms import EducationForm

class CVPageTest(TestCase):

    def test_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html')

class CVEducationTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='tempUser', password='temp')
        self.client.login(username='tempUser', password='temp')
    
    def tearDown(self):
        self.user.delete()

    def test_uses_new_education_template(self):
        response = self.client.get('/cv/education/new/')
        self.assertTemplateUsed(response, 'cv/education_edit.html')

    def test_education_form_valid_data(self):
        form = EducationForm(data={
            'name': 'Test',
            'location': 'Test',
            'start_date': '2019',
            'end_date': '2020',
            'description': 'Test'
        })
        self.assertTrue(form.is_valid())

    def test_education_form_no_data(self):
        form = EducationForm(data = {})
        self.assertFalse(form.is_valid())

    def test_education_form_POST_adds_new_education(self):
        response = self.client.post('/cv/education/new/', {
            'name': 'Test',
            'location': 'Test',
            'start_date': '2019',
            'end_date': '2020',
            'description': 'Test'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(Education.objects.all()), 1)