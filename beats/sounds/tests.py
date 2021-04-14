import pytest
from django.urls import reverse

from beats.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('sounds:sounds'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'title',
    [
        'Beat it',
        'Isn’t she lovely',
    ]
)
def test_title_sound(resp, title):
    assert_contains(resp, title)


def test_content_sound(resp):
    assert_contains(resp, 'src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/412269699')
    assert_contains(resp, 'src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/410849205')
