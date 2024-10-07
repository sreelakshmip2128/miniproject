from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    org_name = models.CharField(max_length=255)
    org_email = models.EmailField(unique=True)
    org_password = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization', null=True)  # Allow null initially
    def __str__(self):
        return self.org_name

class Registers(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)
    user=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.username

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_raised = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # New field to track raised amount
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='campaign_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# Automatically create or update the user profile when the user instance is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

    
