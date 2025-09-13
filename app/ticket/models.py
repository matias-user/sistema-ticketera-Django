from django.db import models
from users.models import CustomUser
from catalog.models import Category, Department, State, Priority

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(blank=False, null=False, max_length=50, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True)
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name="tickets"
    )
    assigned_to = models.ForeignKey(
        CustomUser,
        on_delete= models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tickets" 
    )
    departement = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tickets"
    )
    categories = models.ManyToManyField( 
        Category, 
        related_name="tickets",
        blank=True,
        null=True
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.SET_NULL,
        related_name="tickets",
        blank=True,
        null=True
    )
    state = models.ForeignKey(
        State,
        on_delete=models.SET_NULL,
        related_name="tickets",
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.title
