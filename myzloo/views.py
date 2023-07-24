from rest_framework import generics
from .models import MusicTrack, CustomUser
from .serializers import MusicTrackSerializer, CustomUserSerializer

class MusicTrackListCreateView(generics.ListCreateAPIView):
    queryset = MusicTrack.objects.all()
    serializer_class = MusicTrackSerializer

class MusicTrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MusicTrack.objects.all()
    serializer_class = MusicTrackSerializer

class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
