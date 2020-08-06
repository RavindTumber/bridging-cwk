from django.db import models

class Employment(models.Model):
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.role
        
class Education(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    description = models.TextField() 

    def __str__(self):
        return self.name

class Volunteering(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name
