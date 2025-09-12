from django.contrib import admin
from .models import Category, State, Priority, Department

# Register your models here.
admin.site.register(Category)
admin.site.register(State)
admin.site.register(Priority)
admin.site.register(Department)