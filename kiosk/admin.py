from django.contrib import admin
from kiosk.models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'image', 'price', 'category', 'inventory','slug')
    list_filter=('category', )
    search_fields=('name', 'slug')
    prepopulated_fields={"slug":("name",)}

# Register your models here.
