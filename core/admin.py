from django.contrib import admin
from .models import Item,Order,OrderItem, BillingAdress, Payment, Coupon

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered','start_date']

admin.site.register(Item)
admin.site.register(Coupon)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(BillingAdress)
admin.site.register(Payment)
