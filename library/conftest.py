import factory
import pytest
from faker import Faker
from pytest_factoryboy import register
from rest_framework.test import APIRequestFactory

faker = Faker('pt_BR')


class AuthorFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())

    class Meta:
        model = 'authors.Author'


class BookFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    edition = factory.LazyAttribute(lambda x: faker.pyint())

    class Meta:
        model = 'books.Book'

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for author in extracted:
                self.authors.add(author)


register(AuthorFactory)
register(BookFactory)


@pytest.fixture
def api_request_factory():
    return APIRequestFactory()


@pytest.fixture
def book_data():
    return factory.build(dict, FACTORY_CLASS=BookFactory)
