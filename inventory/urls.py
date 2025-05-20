from django.urls import path
from . import views

urlpatterns = [
    path("", views.showInventory, name="view-inventory"),
    path('add', views.addItem, name="view-addItem"),
]
