from django.shortcuts import render

# Create your views here.

def searchView(request):

    # 将所有的本地变量传过去
    return render(request,'search.html',locals())