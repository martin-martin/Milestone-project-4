from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path("store/", views.store, name="store"),
    path("product_details/<product_id>", views.product_details, name="product_details"),
]