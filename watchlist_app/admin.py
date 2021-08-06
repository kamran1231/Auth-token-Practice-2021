from django.contrib import admin
from .models import WatchList,StreamPlatform,Review
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','rating','watchlist','description','created','update','active']
    list_display_links = ['id','rating']


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ['id','title','platform','storyline','created','active']
    list_display_links = ['id','title']


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['id','name','about','website']
    list_display_links = ['id','name']