from django.db import models
from HelperClasses.AbstractDateModels import AbstractDateModels

# Create your models here.


class TrainType(AbstractDateModels):
    id = models.AutoField(primary_key=True)
    train_type_name = models.CharField(max_length=256)


class CoachCompisition(AbstractDateModels):
    id = models.AutoField(primary_key=True)
    seat_count = models.IntegerField()
    row_number = models.IntegerField()
    column_number = models.IntegerField()
    first_row_seat_counts = models.IntegerField()
    last_row_seat_counts = models.IntegerField(null=True, blank=True)
