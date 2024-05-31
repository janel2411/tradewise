from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username, email=instance.email, first_name=instance.first_name, last_name=instance.last_name)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.username = instance.username
    instance.profile.email = instance.email
    instance.profile.first_name = instance.first_name
    instance.profile.last_name = instance.last_name
    instance.profile.save()