from django.shortcuts import render


def sounds(request, slug):
    sound = {'title': 'Beat it', 'soundcloud_id': 412269699}
    return render(request, 'sounds/sounds.html', context={'sound': sound})
