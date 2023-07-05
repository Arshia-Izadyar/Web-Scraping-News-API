from rest_framework.urls import path
from .views import RegisterUser, ChangePasswords
from rest_framework.authtoken import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register-user"),
    path("chnge-pass/", ChangePasswords.as_view(), name="register-user"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api-token-auth/', views.obtain_auth_token),
]
