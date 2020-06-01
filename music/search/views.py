from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from index.models import *


# Create your views here.

def searchView(request,page):

    if request.method == 'GET':
        search_song = Dynamic.objects.select_related('song').order_by('dynamic_search').all()
        kword = request.session.get('kword','')
        if kword:
            song_info = Song.objects.values()
            pass
        else:
            pass
        # 设置基本数据




        return render(request, 'search.html', locals())
    else:
        # ''是设置为空的默认数据
        request.session['kword'] = request.POST.get('kword','')

        return redirect('/search/1.html')




