from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from rest_framework import viewsets
from .models import InventoryDB
from .serializers import InventorySerializer

def addItem(request):
    context = {}
    if request.method == "GET":
        return render(request, "inventory/addItem.html")
    elif request.method == "POST":
        name = request.POST.get("ingredName")
        amount = request.POST.get("ingredAmount")
        unit = request.POST.get("unitName")

        # Optional validation
        # Validation: check required fields
        if not name or not amount or not unit:
            messages.error(request, "You forgot to put something")
            return redirect("view-addItem")

        try:
            amount = float(amount)
        except ValueError:
            messages.error(request, "Amount must be a number")
            return redirect("view-addItem")

        # Save to DB if all is good
        if InventoryDB.objects.filter(name__iexact=name).exists():
            item = InventoryDB.objects.get(name__iexact=name)
            item.quantity = amount
            item.unit = unit
            item.last_stocked = timezone.now()
            item.save()
            messages.success(request, f"Updated {name} successfully!")
        else:
            InventoryDB.objects.create(
                name=name,
                quantity=amount,
                unit=unit,
                last_stocked=timezone.now()
            )
        messages.success(request, f"Added {name} successfully!!")
        return redirect("view-addItem")
    
def showInventory(request):
    context = {
        "items": InventoryDB.objects.all()
    }

    return render(request, "inventory\showInventory.html", context)

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryDB.objects.all()
    serializer_class = InventorySerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get("name")
        item = InventoryDB.objects.filter(name__iexact=name).first()

        if item:
            item.quantity = serializer.validated_data.get("quantity")
            item.unit = serializer.validated_data.get("unit")
            item.last_stocked = timezone.now()
            item.expiry_date = serializer.validated_data.get("expiry_date")
            item.save()
            serializer.instance = item
        else:
            serializer.save(last_stocked=timezone.now())