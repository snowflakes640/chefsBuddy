from rest_framework import serializers
from .models import InventoryDB

class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryDB
        fields = ("id", "name", "quantity", "unit", "expiry_date", "last_stocked")