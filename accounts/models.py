from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		"""
        Creates and saves a User with the given email, date of
        birth and password.
        """
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
            email=self.normalize_email(email),
            username=username
        )
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password=None):
		"""
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
		user = self.create_user(
            email,
            password=password,
            username=username
        )
		user.is_admin = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	email = models.EmailField(verbose_name='email address', max_length=255, unique=True, null=True )
	username = models.CharField(max_length=200, unique=True, null=True)
	phone = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	
	objects = MyUserManager()
	
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']


	def __str__(self):
		return self.email
	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
		return True
		
	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin
