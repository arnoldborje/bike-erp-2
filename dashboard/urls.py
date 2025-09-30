from django.urls import  path, include

from .views import dashboard_page

urlpatterns = [
    path('', dashboard_page, name='dashboard_page'),
    path('bike/', include('bikes.urls')),
    path('sale/', include('sales.urls')),
    path('repair/', include('repairs.urls')),
    path('employee/', include('employee.urls')),
]
