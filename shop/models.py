from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price_cents = models.IntegerField()

    def __str__(self) -> str:
        return self.name
