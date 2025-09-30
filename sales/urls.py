from django.urls import path
from .views import sale_list_page, sale_detail_page, sale_add_page

urlpatterns = [
    path("", sale_list_page, name="sale_list_page"),
    path("<int:pk>/", sale_detail_page, name="sale_detail_page"),
    path("add/", sale_add_page, name="sale_add_page"),
]