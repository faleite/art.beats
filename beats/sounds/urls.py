from django.urls import path

from beats.sounds.views import sound

app_name = 'sounds'
urlpatterns = [
    path('sounds', sound, name='sounds'),
]
