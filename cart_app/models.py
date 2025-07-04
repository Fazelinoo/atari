from django.db import models
from django.contrib.auth.models import User
from Daroos_app.models import Daroo

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    product = models.ForeignKey(Daroo, on_delete=models.CASCADE, null=True,)
    quantity = models.PositiveIntegerField(default=1, null=True,)
    address = models.TextField(null=True,)
    phone_number = models.CharField(max_length=20, null=True,)
    created_at = models.DateTimeField(auto_now_add=True, null=True,)

    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Daroo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.title} × {self.quantity}"
