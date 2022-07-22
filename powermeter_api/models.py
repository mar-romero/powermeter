from django.db import models

# Create your models here.


class Mediciones(models.Model):
    mediciones = models.FloatField()
    def __str__(self):
        return self.mediciones
