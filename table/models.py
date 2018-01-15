from django.db import models

# Create your models here.
class ReservationStatus(models.Model):
    floor_table_no = models.CharField(max_length=100)
    status   = models.CharField(max_length=100, default="Vacancy")
