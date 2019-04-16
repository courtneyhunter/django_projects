from django.db import models

class category(models.Model) :
    name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self) :
        return self.category

class iso(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self) :
        return self.iso

class region(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self) :
        return self.region

class states(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.state

class site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=550)
    year = models.IntegerField(null=True)
    justification = models.CharField(max_length=550)
    iso = models.ForeignKey(iso, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(region, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(states, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True, default=None)
    latitude = models.FloatField(null=True, blank=True, default=None)
    area_hectares = models.FloatField(null=True, blank=True, default=None)

    def __str__(self) :
        return self.name
