# created to create a profile automatically whenever a user is created
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# a receiver is a fuction that gets a signal and then performs some tasks
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
# '**kwargs' accepts any addition keyword arguments onto the end of the function
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
