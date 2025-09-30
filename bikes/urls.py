from django.urls import  path

from .views import bike_add_page, bike_detail_page, bike_edit_page, bike_list_page, bike_delete_page

urlpatterns = [
    path('', bike_list_page, name='bike_list_page'),
    path('add/', bike_add_page, name='bike_add_page'),
    path('detail/<int:pk>/', bike_detail_page, name='bike_detail_page'),
    path('<int:pk>/edit/', bike_edit_page, name='bike_edit_page'),
    path('<int:pk>/delete/', bike_delete_page, name='bike_delete_page'),
]
