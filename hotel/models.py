from django.db import models

# Create your models here.
class items(models.Model):
    name=models.CharField(max_length=80)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.CharField(max_length=2500)

    