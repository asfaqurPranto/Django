from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save # Produce a signal if there is any database action.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE )
    profession = models.CharField(max_length=150, null=True, blank=True)
    
    # additional field
    phone = models.CharField(max_length=30, null=True, blank=True)
    # address = models.CharField(max_length=250, null=True, blank=True)
    profile_username = models.CharField(max_length=150, unique=False, default='default_username')
    city = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True,default="Bangladesh")
    profession = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField()
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return "{0}".format(self.user.email)
# When any User instance created, Profile object instance is created automatically linked by User 
@receiver(post_save, sender = User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)
    else:
        instance.profile.save()