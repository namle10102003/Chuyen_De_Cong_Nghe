from django.db import models

class NewManager(models.Manager):
    pass

class ExtraManagers(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True
