from django.db import models
from django.core import validators

class Product(models.Model):
    id = models.BigAutoField(
        primary_key = True
    )

    name = models.CharField(
        max_length = 70,
        verbose_name = 'Product Name'
    )

    description = models.TextField(
        max_length = 700,
        verbose_name = 'Description'
    )

    price = models.FloatField(
        verbose_name = 'price',
        validators = [
            validators.MinValueValidator(50),
            validators.MinValueValidator(100000)
        ]
    )