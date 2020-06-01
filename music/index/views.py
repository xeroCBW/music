from django.shortcuts import render
# 导入所有的类
from .models import *
# Create your views here.
def indexView(request):


    # 设置基本数据
    search_song = Dynamic.objects.select_related('song').order_by('dynamic_search').all()

    label_list = Label.objects.all()

    play_hot_song = Dynamic.objects.select_related('song').order_by('dynamic_plays').all()[:10]

    daily_recommendation = Song.objects.order_by('song_release').all()[:3]

    search_ranking = search_song[:6]

    down_ranking = Dynamic.objects.select_related('song').order_by('dynamic_down').all()[:6]

    all_ranking = [search_ranking,down_ranking]

    # 将所有的local传过去

    # for s in search_song:
    #     print(s)

    return render(request,'index.html',locals())



# 自定义404和500的错误页面
def page_not_found(request):
    return render(request, 'error404.html', status=404)