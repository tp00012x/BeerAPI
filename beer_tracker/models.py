from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class BeerModel(models.Model):

    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=254, default="")
    style = models.CharField(max_length=254, default="")
    ibu = models.IntegerField(default="")
    calories = models.IntegerField(default="")
    abv = models.IntegerField(default="")
    location = models.CharField(max_length=254, default="")

    class Meta:
        verbose_name_plural = 'Beers'

    def __str__(self):
        return self.name

class RateModel(models.Model):

    FIVE_REVIEWS = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )

    TEN_REVIEWS= (
        ('10', '10'),
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

    beer = models.ForeignKey(BeerModel)
    aroma = models.CharField(max_length=2, choices=FIVE_REVIEWS, default="--")
    appearance = models.CharField(max_length=2, choices=FIVE_REVIEWS, default="--")
    taste = models.CharField(max_length=2, choices= TEN_REVIEWS, default= "--")
    overall = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Ratings'