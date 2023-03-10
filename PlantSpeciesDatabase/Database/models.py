from django.db import models
class DatabaseModel(models.Model):
    plant_name=models.CharField(max_length=100)
    plant_family=models.CharField(max_length=100)

    plant_des=models.TextField()

# Create your models here.
