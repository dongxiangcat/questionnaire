# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Theme
from .forms import AddThemeForm
from utils import mp_render
# Create your views here.

#首页
def index(request):
    try:
        theme = Theme.objects.latest()
        context = {}
        context['theme'] = theme
    except:
        return mp_render(request,'404.html')
    else:
        #return HttpResponse(utils.a())
        return mp_render(request,'index.html',context)


def addTheme(request):
    if request.method == 'POST':
        form = AddThemeForm(request.POST)
        if form.is_valid():
            theme = Theme()
            theme.title = form.cleaned_data['title']
            theme.description = form.cleaned_data['description']
            theme.save()
    else:
        form = AddThemeForm()
        return render(request,'background/addTheme.html',{'form':form})


