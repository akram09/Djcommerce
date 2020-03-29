from django.urls import path
from .views import (
HomeView,ItemDetailView, add_to_cart, remove_from_cart,OrderSummary,CheckoutView,
add_quantity, minus_quantity , delete_product
)
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('item/<slug>/' , ItemDetailView.as_view(), name="item"),
    path('cart_summary/' , OrderSummary.as_view(), name="cart-summary"),
    path('cart_summary/add/<slug>/' , add_quantity, name="add-quantity"),
    path('cart_summary/remove/<slug>/' , delete_product, name="remove-product"),
    path('cart_summary/minus/<slug>/' , minus_quantity, name="minus-quantity"),
    path('checkout/' , CheckoutView.as_view(), name="checkout"),
    path('add_to_cart/<slug>/', add_to_cart , name="add_to_cart"),
    path('remove_from_cart/<slug>/', remove_from_cart , name="remove_from_cart")
]
