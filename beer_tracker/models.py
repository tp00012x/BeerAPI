from django.db import models
from django.conf import settings

# Models

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

    def avg(self):
        return


class RateModel(models.Model):

    FIVE_REVIEWS = (
        (5, 5),
        (4, 4),
        (3, 3),
        (2, 2),
        (1, 1),
    )

    TEN_REVIEWS= (
        (10, 10),
        (9, 9),
        (8, 8),
        (7, 7),
        (6, 6),
        (5, 5),
        (4, 4),
        (3, 3),
        (2, 2),
        (1, 1),
    )

    user = models.ForeignKey(User, default=1)
    beer = models.ForeignKey(BeerModel)
    aroma = models.PositiveIntegerField(choices=FIVE_REVIEWS, default="5")
    appearance = models.PositiveIntegerField(choices=FIVE_REVIEWS, default="5")
    taste = models.PositiveIntegerField(choices= TEN_REVIEWS, default= "10")

    class Meta:
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return str(self.beer)