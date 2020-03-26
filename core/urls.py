from django.urls import path
from .views import HomeView,ItemDetailView, add_to_cart, remove_from_cart
urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('item/<slug>/' , ItemDetailView.as_view(), name="item"),
    path('add_to_cart/<slug>/', add_to_cart , name="add_to_cart"),
    path('remove_from_cart/<slug>/', remove_from_cart , name="remove_from_cart")
]
