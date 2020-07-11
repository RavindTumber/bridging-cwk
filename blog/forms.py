from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post # Post model to be used for this form
        fields = ('title', 'text',)