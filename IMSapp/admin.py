from django.contrib import admin
from .models import Items,StockIn,StockOut  # Adjust the import path based on your project structure

admin.site.register(Items)
admin.site.register(StockIn)
admin.site.register(StockOut)
