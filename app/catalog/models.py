from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class State(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=100)
    is_final = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class Priority(models.Model):
    CHOICES_PRIOIRTY = {
        '1':'low',
        '2':'medium',
        '3':'high',
        '4':'critical',
    }
    name = models.CharField(unique=True, blank=False, null=False, max_length=100)
    level = models.CharField(choices=CHOICES_PRIOIRTY)

    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=100)
    description = models.CharField(max_length=200)

