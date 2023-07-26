
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly, IsAuthenticatedOrCreateOnly
from .models import MusicTrack
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CustomUser, myzloo_favorites
from .serializers import CustomUserSerializer, MusicTrackSerializer, FavoritesSerializer


class MusicTrackListCreateView(generics.ListCreateAPIView):
    queryset = MusicTrack.objects.all()
    serializer_class = MusicTrackSerializer
    permission_classes = [IsAdminOrReadOnly]

class MusicTrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MusicTrack.objects.all()
    serializer_class = MusicTrackSerializer
    permission_classes = [IsAdminOrReadOnly]

class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrCreateOnly]

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=True, methods=['get'])
    def favorites(self, request, pk=None):
        user = self.get_object()
        favorites_tracks = myzloo_favorites.objects.filter(user=user)
        serializer = FavoritesSerializer(favorites_tracks, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def toggle_favorite(self, request, pk=None):
        user = self.get_object()
        track_id = request.data.get('track_id')

        try:
            track = MusicTrack.objects.get(pk=track_id)
            if track in user.favorites.all():
                user.favorites.remove(track)
                return Response({"message": "Track removed from favorites"}, status=status.HTTP_200_OK)
            else:
                user.favorites.add(track)
                return Response({"message": "Track added to favorites"}, status=status.HTTP_200_OK)
        except MusicTrack.DoesNotExist:
            return Response({"error": "Track not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddRemoveFavoriteView(generics.GenericAPIView):
    queryset = MusicTrack.objects.all()
    serializer_class = MusicTrackSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]  #

    def post(self, request, pk):
        user = request.user

        try:
            track = MusicTrack.objects.get(pk=pk)
            favorite, created = myzloo_favorites.objects.get_or_create(user=user, track=track)

            if created:
                return Response({'message': 'Added to favorites'}, status=status.HTTP_201_CREATED)
            else:
                favorite.delete()
                return Response({'message': 'Removed from favorites'}, status=status.HTTP_200_OK)
        except MusicTrack.DoesNotExist:
            return Response({'message': 'Music track not found'}, status=status.HTTP_404_NOT_FOUND)



