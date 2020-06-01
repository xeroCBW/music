from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns = [

    path('',views.rankingView,name='ranking'),
    path('.list',views.RankingList.as_view,name='rankingList')

]