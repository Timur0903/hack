from django.contrib import admin
from .models import MusicTrack

class MusicTrackAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

admin.site.register(MusicTrack, MusicTrackAdmin)