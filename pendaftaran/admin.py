from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kamar', 'harga', 'lama_inap')
    search_fields = ('nama', 'kamar')
