from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"api", InventoryViewSet)

urlpatterns = [
    path("", showInventory, name="view-inventory"),
    path('add', addItem, name="view-addItem"),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls"))
]
