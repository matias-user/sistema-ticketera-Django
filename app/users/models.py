from django.db import models
from django.contrib.auth.models import User
from catalog.models import Department
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        'CustomUser',
        on_delete=models.CASCADE
    )
    phone = models.IntegerField(null=True, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.user.username

class CustomUser(AbstractUser):
    name = models.CharField( max_length=100, verbose_name='Nombre' )
    lastname = models.CharField( max_length=100, verbose_name='Apellido' )
    dni = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
            regex=r'^[0-9]{7,8}-[0-9Kk]$',
            message="El RUT debe estar en formato 12345678-9 o 12345678-K",
            code="invalid_rut"
        )],
        verbose_name='RUT'
    )

    def __str__(self) -> str:
        return self.name