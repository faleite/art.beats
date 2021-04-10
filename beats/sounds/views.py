from django.shortcuts import render


def sounds(request, slug):
    return render(request, 'sounds/sounds.html')
