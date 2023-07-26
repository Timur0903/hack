from rest_framework import serializers
from .models import MusicTrack, CustomUser, myzloo_favorites

class MusicTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicTrack
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    favorites = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'favorites')

class FavoritesSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    track = MusicTrackSerializer()

    class Meta:
        model = myzloo_favorites
        fields = ('user', 'track')