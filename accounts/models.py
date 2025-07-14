# accounts/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=11, verbose_name="شماره موبایل")

    def __str__(self):
        return f"{self.user.username} - پروفایل"

# سیگنال برای ساخت پروفایل خودکار هنگام ساخت کاربر
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

