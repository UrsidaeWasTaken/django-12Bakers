from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Baker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profiles', default='no_image.png')
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username


def create_baker(sender, instance, created, **kwargs):
    if created:
        user_profile = Baker.objects.create(user=instance)

post_save.connect(create_baker, sender=User)
