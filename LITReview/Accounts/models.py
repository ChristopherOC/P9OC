from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Ticket(models.Model):
    title = models.fields.CharField(max_length= 1238, verbose_name='Titre')
    descritpion = models.fields.TextField(max_length=2048, blank= True, verbose_name='Description')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Utilisateur')
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=30, unique= True)
#     password = models.CharField(max_length=30)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['password']

#     def __str__(self):
#         return self.username