from django.db import models
from django.conf import settings
# from Accounts.models import MyCustomUser

# Create your models here.
class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

# class FindUser:
#     @staticmethod
#     def search(query):
#         users = MyCustomUser.objects.filter(username__icontains=query)
#         return users