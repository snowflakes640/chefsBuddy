from django.db import models

class InventoryDB(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=20)
    expiry_date = models.DateField(null=True)
    last_stocked = models.DateField(auto_now=True)

    def __str__(self):
        return self.name