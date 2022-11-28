from django.db import models
from HelperClasses.AbstractDateModels import AbstractDateModels

# Create your models here.


class TrainType(AbstractDateModels):
    id = models.AutoField(primary_key=True)
    train_type_name = models.CharField(max_length=256)
