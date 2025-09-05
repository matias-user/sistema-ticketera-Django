from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    # Category
    path('category/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Department
    path('department/add/', views.DepartmentCreateView.as_view(), name='department_add'),
    path('department/<int:pk>/edit/', views.DepartmentUpdateView.as_view(), name='department_edit'),
    path('department/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),

    # Priority
    path('priority/add/', views.PriorityCreateView.as_view(), name='priority_add'),
    path('priority/<int:pk>/edit/', views.PriorityUpdateView.as_view(), name='priority_edit'),
    path('priority/<int:pk>/delete/', views.PriorityDeleteView.as_view(), name='priority_delete'),

    # State
    path('state/add/', views.StateCreateView.as_view(), name='state_add'),
    path('state/<int:pk>/edit/', views.StateUpdateView.as_view(), name='state_edit'),
    path('state/<int:pk>/delete/', views.StateDeleteView.as_view(), name='state_delete'),

]