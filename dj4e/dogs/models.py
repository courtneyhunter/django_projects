from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator

class Type(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Type must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Dog(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
