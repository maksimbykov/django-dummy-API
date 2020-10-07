from django.db import models

class ObjectType(models.Model):
    identifier = models.IntegerField(default=1)
    name = models.CharField(max_length=200)

class Object(models.Model):
    identifier = models.IntegerField(default=1)
    objectType = models.ForeignKey(ObjectType, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)


    