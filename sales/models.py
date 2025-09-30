from django.db import models
from django.contrib.auth.models import User
from bikes.models import Bike

class Sale(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name="sales")
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(blank=True, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bike.brand} {self.bike.model} sold to {self.customer_name}"
    
    @property
    def profit(self):
        return self.selling_price - self.bike.total_cost