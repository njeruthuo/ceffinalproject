from django.contrib import admin
from .models import Blog, Gallery, Event

# TODO: REMOVE GROUP FROM ADMIN PANEL


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'pub_date')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    # list_display = ('title', 'organizer', 'start_date',
    #                 'end_date', 'category', 'location')
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
