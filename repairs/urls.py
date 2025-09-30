from django.urls import  path

from .views import repair_add_page, repair_delete_page, repair_edit_page, repair_list_page, repair_detail_page  


urlpatterns = [
    path('', repair_list_page, name='repair_list_page'),
    path('add/', repair_add_page, name='repair_add_page'),
    path('detail/<int:pk>/', repair_detail_page, name='repair_detail_page'),
    path('<int:pk>/edit/', repair_edit_page, name='repair_edit_page'),
    path('<int:pk>/delete/', repair_delete_page, name='repair_delete_page'),
]