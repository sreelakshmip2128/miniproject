# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# from django.contrib.auth.models import AbstractUser, Group, Permission

# class User(AbstractUser):
#     is_organization = models.BooleanField(default=False)
    
#     # Add related_name attributes to avoid conflicts
#     groups = models.ManyToManyField(
#         Group,
#         related_name='myapp_user_set',
#         blank=True,
#         help_text='The groups this user belongs to.',
#         verbose_name='groups',
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='myapp_user_set',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )

# class Organization(models.Model):
#     name = models.CharField(max_length=255)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# # class Campaign(models.Model):
# #     title = models.CharField(max_length=200)
# #     description = models.TextField()
# #     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
# #     verified = models.BooleanField(default=False)  # Shows if verified by an organization

# # class Donation(models.Model):
# #     campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
# #     amount = models.DecimalField(max_digits=10, decimal_places=2)
# #     donor = models.ForeignKey(User, on_delete=models.CASCADE)

# # class VerificationRequest(models.Model):
# #     campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)
# #     organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
# #     requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
# #     status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
# #     requested_on = models.DateTimeField(auto_now_add=True)

    
#     def __str__(self):
#         return self.title


from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    org_name = models.CharField(max_length=255)
    org_email = models.EmailField(unique=True)
    org_password = models.CharField(max_length=50)

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
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Use ForeignKey for a many-to-one relationship

    def __str__(self):
        return self.title
    
