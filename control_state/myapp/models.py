from django.db import models
from datetime import datetime
# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    right = models.CharField(max_length=12)
    def __str__(self):
        return self.username
    class Meta:
        db_table = "users"

class Station(models.Model):
    station_id = models.IntegerField()
    name = models.CharField(max_length=6)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "station"

class info_data (models.Model):
    Lng = models.FloatField()
    Lat = models.FloatField()
    Bat = models.FloatField()
    height = models.FloatField()
    UAViffly = models.SmallIntegerField()
    ifin = models.SmallIntegerField()
    staOK = models.SmallIntegerField()
    conmuOK = models.SmallIntegerField()
    station_id = models.IntegerField()
    time = models.DateTimeField(default=datetime.now)

    def __int__(self):
        return self.station_id
    class Meta:
        db_table = 'info_data'

class mission(models.Model):
    station_id = models.IntegerField()
    Chang = models.IntegerField()
    Wei = models.IntegerField()
    Path = models.IntegerField()
    time = models.DateTimeField(default=datetime.now)

    def __int__(self):
        return self.station_id
    class Meta:
        db_table = 'mission'

class info_muchao(models.Model):
    station_id = models.IntegerField()
    wendu = models.FloatField()
    shidu = models.FloatField()
    fengsu = models.FloatField()
    yuliang = models.FloatField()
    state = models.IntegerField()
    time = models.DateTimeField(default=datetime.now)

    def __int__(self):
        return self.station_id
    class Meta:
        db_table = 'muchao'






