from django.db import models
from apps.core.models import BaseModel
from apps.customers.models import Customer

class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField()
    order_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Order {self.id} for {self.customer.name}"