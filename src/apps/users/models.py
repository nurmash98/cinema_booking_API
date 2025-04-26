from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role='user'):
        if not email:
            raise ValueError("Email is required")
        
        user = self.model(email=self.normalize_email(email), role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None):
        return self.create_user(email, password, role="admin")
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
