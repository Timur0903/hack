from django.contrib import admin
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis

from .models import MusicTrack

class MusicTrackAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        audio_path = obj.audio_file.path

        try:
            if audio_path.lower().endswith('.mp3'):
                audio = MP3(audio_path)
                duration_seconds = int(audio.info.length)
            elif audio_path.lower().endswith('.flac'):
                audio = FLAC(audio_path)
                duration_seconds = int(audio.info.length)
            elif audio_path.lower().endswith('.ogg'):
                audio = OggVorbis(audio_path)
                duration_seconds = int(audio.info.length)
            else:
                duration_seconds = 0

            # Установить вычисленное значение в поле duration_seconds
            obj.duration_seconds = duration_seconds
        except Exception as e:
            print(f"Error calculating duration_seconds: {e}")
            obj.duration_seconds = 0

        obj.save()

admin.site.register(MusicTrack, MusicTrackAdmin)
