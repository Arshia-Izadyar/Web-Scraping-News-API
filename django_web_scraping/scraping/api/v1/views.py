from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from scraping.models import News

from .serializer import NewsSerializer
from .paginator import NewsPaginator


class NewsList(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = NewsPaginator
    filter_backends = [SearchFilter]
    search_fields = ["title", "source"]
