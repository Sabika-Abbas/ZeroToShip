from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    major = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    last_contacted_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Interaction(models.Model):
    INTERACTION_TYPES = [
        ('coffee', 'Coffee Chat'),
        ('hackathon', 'Hackathon'),
        ('email', 'Email'),
        ('career_fair', 'Career Fair'),
        ('lecture', 'Guest Lecture'),
        ('other', 'Other'),
    ]

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='interactions')
    interaction_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=INTERACTION_TYPES, default='other')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.contact.name} - {self.get_type_display()}"