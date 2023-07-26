from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from account.views import RegistrationView, ActivationView, LoginView, UserListView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('', UserListView.as_view()),
]

