from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    class Genre(models.TextChoices):

        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'Ar'

    name = models.fields.CharField(max_length=100)

    genre = models.fields.CharField(max_length=50)

    biography = models.fields.CharField(max_length=1000)

    # description = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
