from django.urls import path, include
from .views import NewsList


urlpatterns = [
    path("news/", NewsList.as_view(), name="news-list"),
    path("accounts/", include("accounts.api.v1.urls")),
]
