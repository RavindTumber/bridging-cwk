from django import forms

from .models import Education, Volunteering

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('name', 'location', 'start_date', 'end_date', 'description',)

class VolunteeringForm(forms.ModelForm):

    class Meta:
        model = Volunteering
        fields = ('name', 'location', 'start_date', 'end_date', 'description',)