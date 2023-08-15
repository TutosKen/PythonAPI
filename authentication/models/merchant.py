from django.db import models

# Create your models here.


class Merchant(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'merchant'
