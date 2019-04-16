from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class House(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
            max_length=200,
            help_text='Enter a house (e.g. Dodge)',
            validators=[MinLengthValidator(2, "House must be greater than 1 character")]
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Wizard(models.Model) :
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "House must be greater than 1 character")]
    )
    power = models.PositiveIntegerField()
    spell = models.CharField(max_length=300)
    house = models.ForeignKey('House', on_delete=models.CASCADE, null=False)

    # Shows up in the admin list
    def __str__(self):
        return self.nickname
