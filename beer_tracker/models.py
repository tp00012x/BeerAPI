from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class Beer(models.Model):
    pass


class Glass(models.Model):
    pass


class Review(models.Model):
    pass

