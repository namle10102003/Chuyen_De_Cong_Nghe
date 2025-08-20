from django.db import models

class CustomQuerySet(models.QuerySet):
    # Thêm các phương thức tùy chỉnh cho QuerySet ở đây nếu cần
    pass

class MyBaseManager(models.Manager):
    # Thêm các phương thức tùy chỉnh cho Manager ở đây nếu cần
    pass

class MyManager(MyBaseManager.from_queryset(CustomQuerySet)):
    use_in_migrations = True

class MyModel(models.Model):
    objects = MyManager()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
