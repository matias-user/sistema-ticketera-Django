from django.views.generic import UpdateView, DeleteView, CreateView, TemplateView

from catalog.models import Category, Department, Priority, State
from .forms import CategoryForm, DepartmentForm, PriorityForm, StateForm

# Create your views here.
class ManageEntitiesView(TemplateView):
    template_name = "catalog/manage_entities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['departments'] = Department.objects.all()
        context['priorities'] = Priority.objects.all()
        context['state|'] = State.objects.all()
        context['category_form'] = CategoryForm()
        context['department_form'] = DepartmentForm()
        context['priority_form'] = PriorityForm()
        context['state_form'] = StateForm()
        return context

# Category
class CategoryUpdateView(UpdateView):
    model = Category

class CategoryCreateView(CreateView):
    model = Category

class CategoryDeleteView(DeleteView):
    model = Category

# Department
class DepartmentUpdateView(UpdateView):
    model = Department

class DepartmentCreateView(CreateView):
    model = Department

class DepartmentDeleteView(DeleteView):
    model = Department

# State
class StateUpdateView(UpdateView):
    model = State

class StateCreateView(CreateView):
    model = State

class StateDeleteView(DeleteView):
    model = State

# Priority
class PriorityUpdateView(UpdateView):
    model = Priority

class PriorityCreateView(CreateView):
    model = Priority

class PriorityDeleteView(DeleteView):
    model = Priority

