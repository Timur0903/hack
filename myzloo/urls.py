from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicTrackListCreateView, MusicTrackDetailView, CustomUserViewSet, AddRemoveFavoriteView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('music-tracks/', MusicTrackListCreateView.as_view(), name='music-track-list-create'),
    path('music-tracks/<int:pk>/', MusicTrackDetailView.as_view(), name='music-track-detail'),
    path('users/<int:pk>/favorites/', AddRemoveFavoriteView.as_view(), name='add-remove-favorite'),
    path('users/<int:pk>/toggle_favorite/', CustomUserViewSet.as_view({'post': 'toggle_favorite'})),
]