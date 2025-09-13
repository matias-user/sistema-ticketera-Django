from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class State(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=100)
    is_final = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class Priority(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

