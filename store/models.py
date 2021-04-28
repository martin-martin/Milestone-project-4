from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=150, blank=False, unique=True)
    product_description = models.CharField(max_length=250, blank=False)
    product_price = models.IntegerField(blank=False)
    added_date = models.DateField(blank=False)

    def price_with_vat(self):
        price_with_vat = self.product_price * 1.25

        return int(price_with_vat)

    def __str__(self):
        return self.product_name
