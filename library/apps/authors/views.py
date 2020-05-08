from rest_framework import filters, viewsets

from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A ViewSet for author.

    Automatically provides `list`, `retrieve` actions.

    Additionally provide the possibility to `search` by `name`.
    """
    queryset = Author.objects.order_by('id')
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
