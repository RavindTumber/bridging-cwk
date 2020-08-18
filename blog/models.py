from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(max_length=200)
    text = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title