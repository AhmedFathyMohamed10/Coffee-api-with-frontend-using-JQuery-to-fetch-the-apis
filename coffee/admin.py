from django.contrib import admin
from .models import Coffee, CoffeeImageModel

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'is_available')

admin.site.register(Coffee, CoffeeAdmin)


class CoffeeImageModelAdmin(admin.ModelAdmin):
    list_display = ('coffee', 'image')

admin.site.register(CoffeeImageModel, CoffeeImageModelAdmin)