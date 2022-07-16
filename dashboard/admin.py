from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'MarketStock'

admin.site.register(Product)
admin.site.unregister(Group)
admin.site.register(Order)

