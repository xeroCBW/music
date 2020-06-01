from django.shortcuts import render

# Create your views here.
def playView(request):

    
    return render(request,'play.html',locals())


def downloadView(request):

    return None