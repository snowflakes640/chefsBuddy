from django.contrib import admin
from .models import InventoryDB

# admin.site.register(InventoryDB)

@admin.register(InventoryDB)
class InventoryDBAdmin(admin.ModelAdmin):
    # Show these fields in the admin list view (table)
    list_display = ("id", 'name', 'quantity', 'unit', 'expiry_date', 'last_stocked')

    # Make last_stocked visible in the detail view (as read-only)
    readonly_fields = ("id", 'last_stocked',)