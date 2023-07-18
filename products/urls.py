from django.urls import path
from . import views



urlpatterns = [
    path("", views.Products_List, name="Products"),
    path('<int:id>/', views.Products_Detail, name="detail"),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]

