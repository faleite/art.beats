import pytest
from django.urls import reverse

from beats.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('sounds:sounds', args=('beat-it',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_sound(resp):
    assert_contains(resp, '<h2>Beat it</h2>')


def test_content_sound(resp):
    assert_contains(resp, 'src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/412269699')
