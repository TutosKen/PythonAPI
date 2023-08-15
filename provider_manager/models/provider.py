from django.db import models

# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "provider"
