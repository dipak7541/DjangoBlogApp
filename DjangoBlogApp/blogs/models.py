from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class AutherRegistration(AbstractUser):
    profileimage = models.ImageField(upload_to='images/')
    middle_name = models.CharField(max_length=150, blank=True)
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
        (2, 'not specified'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)


class BlogModel(models.Model):
    auther = models.ForeignKey(AutherRegistration, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
