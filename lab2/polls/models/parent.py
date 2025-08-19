from django.db import models

class ParentModel(models.Model):
    class Meta:
        pass

class ChildModel(ParentModel):
    class Meta:
        ordering = []
