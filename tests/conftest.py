import pytest

from naipy import client, sync


@pytest.fixture
def search():
    return client.Search()


@pytest.fixture
def trans():
    return client.Translation()


@pytest.fixture
def sync_search():
    return sync.Search()


@pytest.fixture
def sync_trans():
    return sync.Translation()
