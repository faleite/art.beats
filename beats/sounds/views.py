from django.shortcuts import render


def sound(request):
    sounds = [
        {'slug': 'beat-it', 'title': 'Beat it', 'soundcloud_id': 412269699},
        {'slug': 'isnt-she-lovely', 'title': 'Isn’t she lovely', 'soundcloud_id': 410849205},
    ]
    return render(request, 'sounds/sounds.html', context={'sounds': sounds})

# sounds_dct = {dct['slug']: dct for dct in sounds}
