from django.db import models

class CigCollector(models.Model):
    name = models.CharField('name', max_length=20, unique=True, null=False)
    latitude = models.FloatField('latitude', null=False)
    longitude = models.FloatField('longitude', null=False)
    district = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.name