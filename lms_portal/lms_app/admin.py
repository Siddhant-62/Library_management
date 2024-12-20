from django.contrib import admin
from .models import Reader

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'reader_name', 'reader_contact', 'reference_id', 'reader_address')
    search_fields = ('reader_name', 'reader_contact', 'reference_id')

