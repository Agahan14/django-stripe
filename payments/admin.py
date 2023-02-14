from django.contrib import admin

# Register your models here.
from payments.models import (
    Item,
    Order,
    Discount,
    Tax,
)

admin.site.register([Item, Order, Discount, Tax])
