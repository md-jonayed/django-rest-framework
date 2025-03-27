from django.db import models

class Phones(models.Model):
    name=models.CharField(max_length=256)
    releasedYear=models.CharField(max_length=10)
    processorName=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.name+"-"+self.releasedYear