from django.urls import path, include
from rest_framework import routers
from .views import InventoryViewSet

router = routers.DefaultRouter()
router.register(r"", InventoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("api-auth/", include("rest_framework.urls"))
]

# | **HTTP Method** | **URL**      | **DRF Action**      |
# | --------------- | ------------ | ------------------- |
# | GET             | `/api/`      | `.list()`           |
# | POST            | `/api/`      | `.create()`         |
# | GET             | `/api/{id}/` | `.retrieve()`       |
# | PUT             | `/api/{id}/` | `.update()`         |
# | PATCH           | `/api/{id}/` | `.partial_update()` |
# | DELETE          | `/api/{id}/` | `.destroy()`        |
