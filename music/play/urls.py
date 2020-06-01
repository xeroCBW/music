from django.urls import path
from . import views

urlpatterns = [

    path('<int:song_id>.html',views.playView,name='play'),
    path('down/<int:song_id>.html',views.downloadView,name='download')

]