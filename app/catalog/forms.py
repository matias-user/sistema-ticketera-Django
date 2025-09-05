from django import forms
from .models import Department, State, Priority, Category

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name']

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

