from django.shortcuts import render
# 导入所有的类
from .models import *
# Create your views here.
def indexView(request):


    # 设置基本数据
    search_song = Dynamic.objects.select_related('song').order_by('dynamic_search').all()[:8]

    label_list = Label.objects.all()

    play_hot_song = Dynamic.objects.select_related('song').order_by('dynamic_plays').all()[:10]


    daily_recommendation = Song.objects.order_by('song_release').all()[:3]

    search_ranking = search_song[:6]

    down_ranking = Dynamic.objects.select_related('song').order_by('dynamic_down').all()[:6]

    all_ranking = [search_ranking,down_ranking]

    # 将所有的local传过去

    # for s in search_song:
    #     print(s.values())






    return render(request,'index.html',locals())