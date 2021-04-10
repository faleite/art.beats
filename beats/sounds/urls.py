from django.urls import path

from beats.sounds.views import sounds

app_name = 'sounds'
urlpatterns = [
    path('<slug:slug>', sounds, name='sounds'),
]
