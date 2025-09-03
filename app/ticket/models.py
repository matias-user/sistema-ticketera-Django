from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(blank=False, null=False, max_length=50, unique=True)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    assigned_to = models.ForeignKey(
        User,
        on_delete= models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tickets" 
    )


    def __str__(self) -> str:
        return self.title
