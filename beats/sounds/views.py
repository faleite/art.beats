from django.shortcuts import render

# sounds = [
#     Sound(slug='beat-it', title='Beat it', soundcloud_id='412269699%3Fsecret_token%3Ds-FuMeock5xrV'),
# ]
#


class Sounds:

    def __init__(self, slug, title, soundcloud_id):
        self.slug = slug
        self.title = title
        self.soundcloud_id = soundcloud_id

    # def get_absolute_url(self):
    #     return reverse('sounds:sounds', args=(self.slug,))


def sound(request):
    sounds = [
        Sounds('beat-it', 'Beat it', '412269699%3Fsecret_token%3Ds-FuMeock5xrV'),
        Sounds('isnt-she-lovely', 'Isn’t she lovely', '410849205'),
    ]
    return render(request, 'sounds/sounds.html', context={'sounds': sounds})


# sounds_dct = {v.slug: v for v in sounds}
