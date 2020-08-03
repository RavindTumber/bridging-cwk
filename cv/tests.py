from django.test import TestCase
from django.contrib.auth.models import User

from .models import Education, Volunteering
from .forms import EducationForm, VolunteeringForm

class CVPageTest(TestCase):

    def test_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html')

class CvEducationTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='tempUser', password='temp')
        self.client.login(username='tempUser', password='temp')
    
    def tearDown(self):
        self.user.delete()

    def test_education_form_valid_data(self):
        form = EducationForm(data={
            'name': 'Test',
            'location': 'Test',
            'start_date': '2019',
            'end_date': '2020',
            'description': 'Test'
        })
        self.assertTrue(form.is_valid(), 'Should be valid if appropriate data is given')

    def test_education_form_no_data(self):
        form = EducationForm(data={})
        self.assertFalse(form.is_valid(), 'Should be invalid if no data is given')

    def test_uses_education_new_template(self):
        response = self.client.get('/cv/education/new/')
        self.assertTemplateUsed(response, 'cv/education_edit.html', 'Authenticated user can access') 

    def test_education_form_POST_adds_new_education(self):
        response = self.client.post('/cv/education/new/', {
            'name': 'Test',
            'location': 'Test',
            'start_date': '2019',
            'end_date': '2020',
            'description': 'Test'
        })
        self.assertEquals(response.status_code, 302, 'Should redirect back to /cv/')
        self.assertEquals(len(Education.objects.all()), 1, 'Should only be one object created')
        self.assertEqual(Education.objects.first().name, 'Test', 'Should have its name be equal to Test')

    def test_uses_education_edit_template(self):
        self.client.post('/cv/education/new/', {
            'name': 'Test',
            'location': 'Test',
            'start_date': '2019',
            'end_date': '2020',
            'description': 'Test'
        })
        education = Education.objects.first()
        response = self.client.get('/cv/education/' + str(education.pk) + '/edit/')
        self.assertTemplateUsed(response, 'cv/education_edit.html', 'Authenticated user can access')
    
    def test_education_edit(self):
        self.client.post('/cv/education/new/', {
            'name': 'Test',
            'location': 'Test',
            'start_date': '2019',
            'end_date': '2020',
            'description': 'Test'
        })
        education = Education.objects.first()
        response = self.client.post('/cv/education/' + str(education.pk) + '/edit/', {
            'name': 'Test edit',
            'location': 'Test edit',
            'start_date': '2019',
            'end_date': '2020',
            'description': 'Test'
        })
        education = Education.objects.first()
        self.assertEqual(response['location'], '/cv/', 'Should point the browser to a new location: /cv/')
        self.assertEquals(len(Education.objects.all()), 1, 'Should only be one object created')
        self.assertEquals(education.name, 'Test edit', 'Should update the education name field')
        self.assertEquals(education.location, 'Test edit', 'Should update the education location field')

    def test_education_delete(self):
        self.client.post('/cv/education/new/', {
            'name': 'Test',
            'location': 'Test',
            'start_date': '2019',
            'end_date': '2020',
            'description': 'Test'
        })
        education = Education.objects.first()
        response = self.client.get('/cv/education/' + str(education.pk) + '/remove/')
        self.assertEqual(response['location'], '/cv/', 'Should point the browser to a new location: /cv/')
        self.assertEquals(len(Education.objects.all()), 0, 'Should be zero education objects')

class CvVolunteeringTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tempUser', password='temp')
        self.client.login(username='tempUser', password='temp')
    
    def tearDown(self):
        self.user.delete()

    def test_volunteering_form_valid_data(self):
        form = VolunteeringForm(data={
            'name': 'Test',
            'location': 'Test',
            'start_date': '2019',
            'end_date': '2020',
            'description': 'Test'
        })
        self.assertTrue(form.is_valid(), 'Should be valid if appropriate data is given')

    def test_volunteering_form_no_data(self):
        form = VolunteeringForm(data={})
        self.assertFalse(form.is_valid(), 'Should be invalid if no data is given')

    def test_uses_volunteering_new_template(self):
        response = self.client.get('/cv/volunteering/new/')
        self.assertTemplateUsed(response, 'cv/volunteering_edit.html', 'Authenticated user can access')

    def test_volunteering_form_POST_adds_new_volunteering(self):
        response = self.client.post('/cv/volunteering/new/', {
            'name': 'Test',
            'location': 'Test',
            'start_date': '2019',
            'end_date': '2020',
            'description': 'Test'
        })
        self.assertEquals(response.status_code, 302, 'Should redirect back to /cv/')
        self.assertEquals(len(Volunteering.objects.all()), 1, 'Should only be one object created')
        self.assertEqual(Volunteering.objects.first().name, 'Test', 'Should have its name be equal to Test')
