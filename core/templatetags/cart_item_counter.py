from core.models import Order
from django import  template
register = template.Library()

@register.filter
def cart_item_counter(user):
    if user.is_authenticated:
        order =Order.objects.filter(user = user , ordered = False)
        if order.exists():
            return order[0].items.count()
    return 0
