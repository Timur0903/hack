from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
from django.contrib.auth import get_user_model
from django.db import models

class MusicTrack(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.PositiveIntegerField()
    duration_seconds = models.PositiveIntegerField(editable=False)
    cover_image = models.ImageField(upload_to='music_covers/', null=True, blank=True)
    audio_file = models.FileField(upload_to='music_tracks/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        audio_path = self.audio_file.path

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

            self.duration_seconds = duration_seconds
        except Exception as e:
            print(f"Error calculating duration_seconds: {e}")
            self.duration_seconds = 0

        print(f"duration_seconds value: {self.duration_seconds}")

        super(MusicTrack, self).save(*args, **kwargs)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    favorites = models.ManyToManyField(MusicTrack, related_name='favorited_by')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class myzloo_favorites(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='favorite_tracks')
    track = models.ForeignKey(MusicTrack, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'track')