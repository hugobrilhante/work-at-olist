from django_filters import rest_framework as filters

from ..authors.models import Author
from .models import Book


class BookFilterSet(filters.FilterSet):
    author = filters.ModelMultipleChoiceFilter(field_name='authors__name', to_field_name='name',
                                               queryset=Author.objects.all(), conjoined=True)

    class Meta:
        model = Book
        fields = ['name', 'publication_year', 'edition', 'author']
