from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    username = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, ID: {self.user.id}, First Name: {self.first_name}, Last Name: {self.last_name}"
