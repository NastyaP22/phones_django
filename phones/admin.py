from django.contrib import admin

from .models import Phone


class PhoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug']
    list_filter = ['price', 'release_date', 'lte_exists']