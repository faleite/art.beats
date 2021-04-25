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


@pytest.mark.parametrize(
    'soundcloud_id',
    [
        '412269699%3Fsecret_token%3Ds-FuMeock5xrV',
        '410849205',
    ]
)
def test_content_sound(resp, soundcloud_id):
    assert_contains(resp, soundcloud_id)


# @pytest.mark.parametrize(
#     'slug',
#     [
#         'beat-it',
#         'isnt-she-lovely',
#     ]
# )
# def test_link_sound(resp, slug):
#     video_link = reverse('sounds:sounds', args=(slug,))
#     assert_contains(resp, f'href"{video_link}"')
