from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_ad')
    list_filter = ('created_ad',)
    search_fields = ('title', 'description')