from django.contrib import admin
from app_music.models import Album, Track,Artist,Tag

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Tag)