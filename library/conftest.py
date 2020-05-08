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


register(AuthorFactory)


@pytest.fixture
def api_request_factory():
    return APIRequestFactory()
