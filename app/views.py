from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_Topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic is inserted')
        else:
            return HttpResponse('data is not valid')
    return render(request,'insert_topic.html',d)
