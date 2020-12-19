import pytest


@pytest.fixture
def get_test_documents():
    return [
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]


@pytest.fixture
def get_test_directories():
    return {
        '1': ['2207 876234', '10006']
    }


@pytest.fixture
def get_new_document():
    return ['passport', '123456', 'John Dow', '1']


@pytest.fixture
def get_document():
    return '10006'


@pytest.fixture
def get_wrong_document():
    return '0000000'


@pytest.fixture
def get_wrong_shelf():
    return '11111111'
