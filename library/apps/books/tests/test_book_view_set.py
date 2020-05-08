import pytest
from rest_framework.reverse import reverse

from ..views import BookViewSet

pytestmark = pytest.mark.django_db


@pytest.fixture
def books(author_factory, book_factory):
    authors = [author_factory() for __ in range(10)]
    books = []
    for author in authors:
        books.append(book_factory(authors=[author]))
    return books


def test_when_list_books(api_request_factory, books):
    url = reverse('book-list')
    request = api_request_factory.get(url)
    view = BookViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.data['count'] == 10


def test_when_create_book(api_request_factory, author, book_data):
    book_data.update({'authors': [author.id]})
    url = reverse('book-list')
    request = api_request_factory.post(url, book_data, format='json')
    view = BookViewSet.as_view({'post': 'create'})
    response = view(request)
    assert response.status_code == 201
    assert response.data['name'] == book_data['name']


def test_when_retrieve_book(api_request_factory, book):
    url = reverse('book-detail', kwargs={'pk': book.pk})
    request = api_request_factory.get(url)
    view = BookViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=book.pk)
    assert response.data['id'] == book.id


def test_when_update_book(api_request_factory, author, book, book_data):
    book_data.update({'id': book.id, 'authors': [author.id]})
    url = reverse('book-detail', kwargs={'pk': book.pk})
    request = api_request_factory.put(url, book_data, format='json')
    view = BookViewSet.as_view({'put': 'update'})
    response = view(request, pk=book.pk)
    assert response.data['name'] == book_data['name']


def test_when_delete_book(api_request_factory, book):
    url = reverse('book-detail', kwargs={'pk': book.pk})
    request = api_request_factory.delete(url)
    view = BookViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=book.pk)
    assert response.status_code == 204


def test_when_filter_books_for_name(api_request_factory, book, books):
    url = reverse('book-list')
    request = api_request_factory.get(url, {'name': book.name})
    view = BookViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.data['count'] == 1


def test_when_filter_books_for_edition(api_request_factory, book, books):
    url = reverse('book-list')
    request = api_request_factory.get(url, {'edition': book.edition})
    view = BookViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.data['count'] == 1


def test_when_filter_books_for_author(api_request_factory, author, book, books):
    book.authors.add(author)
    url = reverse('book-list')
    request = api_request_factory.get(url, {'author': author.name})
    view = BookViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.data['count'] == 1


def test_when_filter_books_for_publication_year(api_request_factory, book, books):
    url = reverse('book-list')
    request = api_request_factory.get(url, {'publication_year': book.publication_year})
    view = BookViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.data['count'] == 1
