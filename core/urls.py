from django.urls import path
from .views import (
HomeView,ItemDetailView, add_to_cart, remove_from_cart,OrderSummary,checkout
)
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('item/<slug>/' , ItemDetailView.as_view(), name="item"),
    path('cart_summary/' , OrderSummary.as_view(), name="cart-summary"),
    path('checkout/' , checkout, name="checkout"),
    path('add_to_cart/<slug>/', add_to_cart , name="add_to_cart"),
    path('remove_from_cart/<slug>/', remove_from_cart , name="remove_from_cart")
]
