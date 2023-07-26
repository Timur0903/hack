"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from myzloo.views import CustomUserListCreateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myzloo.views import MusicTrackListCreateView, MusicTrackDetailView, CustomUserViewSet, AddRemoveFavoriteView

schema_view = get_schema_view(
   openapi.Info(
      title="Music",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny]

)
router = DefaultRouter()



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myzloo.urls')),
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('api/account/', include('account.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include(router.urls)),
    path('music-tracks/', MusicTrackListCreateView.as_view(), name='music-track-list-create'),
    path('music-tracks/<int:pk>/', MusicTrackDetailView.as_view(), name='music-track-detail'),
    path('users/<int:pk>/favorites/', AddRemoveFavoriteView.as_view(), name='add-remove-favorite'),
    path('users/<int:pk>/toggle_favorite/', CustomUserViewSet.as_view({'post': 'toggle_favorite'}),
         name='toggle-favorite'),
    path('api/token/', obtain_auth_token, name='token_obtain_pair'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)