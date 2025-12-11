from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.CharField(max_length=120, null=True, blank=True)
  description = models.TextField(max_length=500, null=True, blank=True)
  date_of_birth = models.DateField(null=True, blank=True)
  phone = models.CharField(max_length=13, null=True, blank=True)
  instagram_user = models.CharField(max_length=100, null=True, blank=True)
  address = models.CharField(max_length=200, null=True, blank=True)
  clints = models.IntegerField(null=True, blank=True)
  hour_worked = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  image = models.ImageField(upload_to="profile", null=True, blank=True)

      
  def __str__(self):
    return f'{self.id} - user id{self.user.id}'

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)