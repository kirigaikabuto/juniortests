from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Distance(models.Model):
    fromCity = models.ForeignKey(City, on_delete=models.CASCADE, related_name="from_city")
    toCity = models.ForeignKey(City, on_delete=models.CASCADE, related_name="to_city")
    distance = models.FloatField()

    def __str__(self):
        return f"{self.fromCity.name} -> {self.toCity.name} ({self.distance})"
