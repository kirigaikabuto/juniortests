from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    coordinateX = models.FloatField(default=0.0)
    coordinateY = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Distance(models.Model):
    fromCity = models.ForeignKey(City, on_delete=models.CASCADE, related_name="from_city")
    toCity = models.ForeignKey(City, on_delete=models.CASCADE, related_name="to_city")
    distance = models.FloatField()

    def __str__(self):
        return f"{self.fromCity.name} -> {self.toCity.name} ({self.distance})"
