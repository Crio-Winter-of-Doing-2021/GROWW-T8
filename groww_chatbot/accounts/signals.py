from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile Created")
        
def save_profile(sender,instance,**kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def update_profile(sender,instance, created, **kwargs):
    if created == False:
        print("Updated Profile")