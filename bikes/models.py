from django.db import models

# Create your models here.
class Bike(models.Model):
    CONDITION_CHOICES = [
        ('fair', 'Fair'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    ]

    STATUS_CHOICES = [
        ('for_repair', 'For Repair'),
        ('ready_to_sell', 'Ready to Sell'),
        ('sold', 'Sold'),
    ]
    
    TYPE_CHOICES = [
        ('whole', 'Whole'),
        ('part', 'Part'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='whole')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="bikes/images/", null=True, blank=True)
    serial_number = models.CharField(max_length=100, unique=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    repair_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='fair')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='for_repair')
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model or ''} - {self.serial_number}"
    
    @property
    def total_cost(self):
        return self.purchase_price + (self.repair_cost or 0)