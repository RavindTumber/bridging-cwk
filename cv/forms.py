from django import forms

from .models import Employment, Education, Volunteering

class EmploymentForm(forms.ModelForm):

    class Meta:
        model = Employment
        fields = {'company_name', 'role', 'location', 'start_date', 'end_date', 'description',}

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('name', 'location', 'start_date', 'end_date', 'description',)

class VolunteeringForm(forms.ModelForm):

    class Meta:
        model = Volunteering
        fields = ('name', 'location', 'start_date', 'end_date', 'description',)