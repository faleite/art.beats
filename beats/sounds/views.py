from django.shortcuts import render


class Sound:

    def __init__(self, slug, title, soundcloud_id):
        self.slug = slug
        self.title = title
        self.soundcloud_id = soundcloud_id


sounds = [
    Sound('beat-it', 'Beat it', '412269699%3Fsecret_token%3Ds-FuMeock5xrV'),
    Sound('isnt-she-lovely', 'Isn’t she lovely', 410849205),
]


def sound(request):
    return render(request, 'sounds/sounds.html', context={'sounds': sounds})


# sounds_dct = {v.slug: v for v in sounds}
