import csv
import os

from django.core.management import CommandError, call_command

import pytest

from library.apps.authors.models import Author


def write_csv_file(name, headers, rows):
    with open(name, 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


@pytest.fixture
def invalid_csv():
    headers = ['invalid']
    rows = [('Invalid Name',)]
    write_csv_file('invalid.csv', headers, rows)


@pytest.fixture
def valid_csv():
    headers = ['name']
    rows = [('Valid name',)]
    write_csv_file('valid.csv', headers, rows)


def test_when_no_csv_file():
    with pytest.raises(CommandError):
        call_command('import_authors')


def test_when_invalid_csv_file(invalid_csv):
    with pytest.raises(CommandError):
        call_command('import_authors', 'invalid.csv')
    os.remove('invalid.csv')


@pytest.mark.django_db
def test_when_valid_csv_file(valid_csv):
    call_command('import_authors', 'valid.csv')
    os.remove('valid.csv')
    author = Author.objects.first()
    assert 'Valid name' == str(author)
