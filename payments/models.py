from django.db import models


class Item(models.Model):
    CURRENCY = (
        ("rub", 'RU'),
        ("usd", 'USD'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0)
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY,
        default="rub",
    )


class Discount(models.Model):
    name = models.CharField(max_length=255)
    number = models.FloatField(default=1)


class Tax(models.Model):
    name = models.CharField(max_length=255)
    number = models.FloatField(default=1)


class Order(models.Model):
    item = models.ManyToManyField(Item, null=True)
    total_price = models.FloatField(default=0)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.item.all())
        if self.tax:
            total_price = int(total_price + (total_price * self.tax.number / 100))
        if self.discount:
            total_price = int(total_price - (total_price * self.discount.number / 100))
        self.total_price = total_price
        self.save()
