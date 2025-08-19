from django.db import models

class Manufacturer(models.Model):
    pass

class Car(models.Model):
    company_that_makes_it = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
