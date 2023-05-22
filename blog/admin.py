from django.contrib import admin
# from django.contrib.admin.models import
from .models import Blog

# TODO: REMOVE GROUP FROM ADMIN PANEL


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'pub_date')
