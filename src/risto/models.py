from django.db import models


class Reserve(models.Model):
    name  = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.IntegerField()
    date  = models.DateField()
    time  = models.CharField(max_length=10)
    Guests= models.IntegerField()

    def __str__(self):
       return self.name
