from django.shortcuts import render

# Create your views here.
from index.models import *

def rankingView(request):


    search_song = Dynamic.objects.select_related('song').order_by('dynamic_search')

    all_list = Song.objects.values('song_type').distinct()
    song_type = request.GET.get('type','')
    if search_song:
        song_info = Dynamic.objects.select_related('song').filter(song__song_type=song_type)
    else:
        song_info = Dynamic.objects.select_related('song').order_by('dynamic_plays').all()

    return render(request,'ranking.html',locals())