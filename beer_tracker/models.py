from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext
# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)


class Beer(models.Model):

    user = models.ForeignKey(UserProfileInfo)

    ibu = models.IntegerField()

    calories = models.IntegerField()

    abv = models.IntegerField()

    style = models.CharField(max_length=254)

    location = models.CharField(max_length=254)


class Review(models.Model):

    FIVE_REVIEWS = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )

    TEN_REVIEWS= (
        ('10', '19'),
        ('9', '9'),
        ('8', '8'),
        ('7', '7'),
        ('6', '6'),
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )
    user = models.ForeignKey(UserProfileInfo)

    aroma = models.CharField(
        max_length=2,
        choices=FIVE_REVIEWS,
        default="--")

    appearance = models.CharField(
        max_length=2,
        choices=FIVE_REVIEWS,
        default="--")

    taste = models.CharField(
        max_length=2,
        choices= TEN_REVIEWS,
        default= "--")

    overall = models.IntegerField(default=0)

    def get_user(self):
        if self.user:
            return self.user.user_name
        return ugettext('Anonymous')
