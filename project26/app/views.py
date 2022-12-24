from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST.get['Topic']
        T=Topic.objects.get_or_create(Topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic is inserted sucessfully')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        tn=request.POST['Topic']
        n=request.POST['name']
        u=request.POST['url']
        t=Topic.objects.get_or_create(Topic_name=tn)[0]
        t.save()
        w=Webpage.objects.get_or_create(Topic_name=t,name=n,url=u)[0]
        w.save()
        return HttpResponse('successfully inserted Webpage')
    return render(request,'insert_webpage.html',d)
