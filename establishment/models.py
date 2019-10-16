from django.db import models
# from django.contrib.gis.db import models


class Establishment(models.Model):
    name = models.CharField(max_length=255, default='')
    longitude = models.FloatField(db_index=True)
    latitude = models.FloatField(db_index=True)
    # position = models.PointField(max_length=40, null=True)
