import pytest
from rest_framework.reverse import reverse

from ..views import AuthorViewSet

pytestmark = pytest.mark.django_db


@pytest.fixture
def authors(author_factory):
    return [author_factory() for __ in range(10)]


def test_when_list_authors(api_request_factory, authors):
    url = reverse('author-list')
    request = api_request_factory.get(url)
    view = AuthorViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.data['count'] == 10


def test_when_retrieve_author(api_request_factory, author):
    url = reverse('author-detail', kwargs={'pk': author.pk})
    request = api_request_factory.get(url)
    view = AuthorViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=author.pk)
    assert response.data['name'] == author.name


def test_when_search_authors_by_name(api_request_factory, author, authors):
    url = reverse('author-list')
    request = api_request_factory.get(url, {'search': author.name})
    view = AuthorViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.data['count'] == 1
