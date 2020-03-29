from django.contrib import admin
from .models import Item,Order,OrderItem, BillingAdress, Payment
# Register your models here.

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(BillingAdress)
admin.site.register(Payment)
