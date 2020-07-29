from django import forms

from .models import Education

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('name', 'location', 'start_date', 'end_date', 'description',)