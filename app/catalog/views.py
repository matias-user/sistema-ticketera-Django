from django.views.generic import UpdateView, DeleteView, CreateView, TemplateView

from .models import Category, Department, Priority, State
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

#Generic
class BaseEntityView:
    template_name = 'catalog/manage_entities.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.verbose_name
        return context

# Category
class CategoryUpdateView(BaseEntityView, UpdateView ):
    model = Category


class CategoryCreateView(BaseEntityView, CreateView ):
    model = Category



class CategoryDeleteView(BaseEntityView, DeleteView ):
    model = Category
    fields = ['name','description']
    template_name = 'catalog/manage_entities.html'
    

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

