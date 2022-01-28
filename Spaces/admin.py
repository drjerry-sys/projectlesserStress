from django.contrib import admin
from .models import Compound, Room

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    search_fields = ('roomType', 'room_yearlyPrice', 'inspection_price')

@admin.register(Compound)
class CompoundAdmin(admin.ModelAdmin):
    search_fields = ('comp_type', 'comp_name')
    list_display = ('comp_name', 'comp_type', 'swimmingPool')