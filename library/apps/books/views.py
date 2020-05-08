from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import BookFilterSet
from .models import Book
from .serializers import BooksSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for book

    Automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.

    Additionally provide the possibility to filter by `name`, `publication_year`, `edition`, `author`
    """
    queryset = Book.objects.order_by('id')
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilterSet
