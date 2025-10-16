from django.db import models

# Create your models here.
class ckdModel(models.Model):

    Glucose=models.FloatField(default=130)
    BloodPressure=models.FloatField(default=130)
    SkinThickness=models.FloatField(default=20)
    Insulin=models.FloatField(default=85)
    BMI=models.FloatField(default=22.0)
    DiabetesPedigreeFunction=models.FloatField(default=0.45)
    Pregnancies=models.IntegerField(default=2)
    Age=models.IntegerField(default=25)
