from django.db import models
from django.contrib.auth.models import User




class UserPredictModel(models.Model):
    image = models.ImageField(upload_to = 'images/')
    label = models.CharField(max_length=20,default='data')

    def __str__(self):
        return str(self.image)
    

from django.db import models

class Patient_info(models.Model):
    Bp = models.IntegerField()
    Sg = models.IntegerField()  # Example: consider using choices=(...) for gender
    Al = models.IntegerField()
    Su = models.IntegerField()
    Rbc = models.IntegerField()
    Bu = models.IntegerField()  # Example: consider using BooleanField for binary fields
    Sc = models.IntegerField()
    Sod = models.IntegerField()
    Pot = models.IntegerField()
    Hemo = models.FloatField()
    Wbcc = models.IntegerField()
    Rbcc = models.IntegerField()
    Htn = models.IntegerField()
    Class = models.CharField(max_length=100)

    def __str__(self):
        return f"Prediction: {self.Class}"



