# signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            instance.userprofile.save()
        except UserProfile.DoesNotExist:
            # Eğer profil yoksa, yeni oluşturabiliriz
            UserProfile.objects.create(user=instance)
