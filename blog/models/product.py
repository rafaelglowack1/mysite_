from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=60, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.product_name
