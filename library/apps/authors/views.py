from rest_framework import filters, viewsets

from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A ViewSet for `viewing` and `search` author.
    """
    queryset = Author.objects.order_by('id')
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
