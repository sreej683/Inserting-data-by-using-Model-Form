from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse


def insert_topic(request):
    ETO=TopicForm()
    d={'ETO':ETO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse("Topic is created")

    return render(request,'insert_topic.html',d)



def insert_topic_by_MF(request):
    ETMO=TopicModelForm()
    d={'ETMO':ETMO}
    if request.method=='POST':
        EMTDO=TopicModelForm(request.POST)
        if EMTDO.is_valid():
            EMTDO.save()
            return HttpResponse('Topic is created')
        else:
            return HttpResponse('data is invalid')
    return render(request,'insert_topic_by_MF.html',d)




def insert_webpage(request):
    EWO=WebPageForm()
    d={'EWO':EWO}
    if request.method=='POST':
        WFDO=WebPageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            na=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']
            em=WFDO.cleaned_data['email']
            TO=Topic.objects.get(topic_name=tn)
            WO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
            WO.save()
            return HttpResponse('Webpage is created')
    return render(request,'insert_webpage.html',d)


def insert_web_by_MF(request):
    WTMO=WebPageModelForm()
    d={'WTMO':WTMO}
    if request.method=='POST':
        WTDMO=WebPageModelForm(request.POST)
        if WTDMO.is_valid():
            WTDMO.save()
            return HttpResponse('WebPage is created')
        else:
            return HttpResponse('invaid data')
    return render(request,'insert_web_by_MF.html',d)








def insert_accessrecord(request):
    WAO=AccessRecordForm()
    d={'WAO':WAO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            na=AFDO.cleaned_data['name']
            au=AFDO.cleaned_data['author']
            da=AFDO.cleaned_data['date']
            WO=WebPage.objects.get(name=na)
            AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)[0]
            AO.save()
            return HttpResponse('AccessRecord is created')
    return render(request,'insert_accessrecord.html',d)





def insert_access_by_Mf(request):
    ATM=AccessModelForm()
    d={'ATM':ATM}
    if request.method=='POST':
        AFTDO=AccessModelForm(request.POST)
        if AFTDO.is_valid():
            AFTDO.save()
            return HttpResponse('AccessRecord is created')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_access_by_MF.html',d)



