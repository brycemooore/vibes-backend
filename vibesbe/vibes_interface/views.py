from django.shortcuts import render
from django.core.serializers import serialize
# Create your views here.
from django.http import HttpResponse
from .models import User, Song


def index(request):
    # s = Song(title="Hello", artist="Hello")
    # s.save()
    # u = User(username="John", email="brycemooore@gmail.com")
    # u.save()
    # u = User.objects.first().song_set.all()
    # # u.songs.add(Song.objects.get(title="Hello"))
    # data = serialize('json', [u], fields=('username', 'email', 'songs'))
    return HttpResponse(data, content_type='application/json')

