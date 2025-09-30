from django.urls import path
from .views import employee_add_page, employee_delete_page, employee_edit_page, employee_list_page

urlpatterns = [
    path('', employee_list_page, name='employee_list_page'),
    path('add/', employee_add_page, name='employee_add_page'),
    path('<int:pk>/edit/', employee_edit_page, name='employee_edit_page'),
    path('<int:pk>/delete/', employee_delete_page, name='employee_delete_page'),
]