from devtool.models import Devtool
from django.shortcuts import render

def devtool_list(request):
    all = Devtool.objects.all()
    ctx = {
        'all' : all,
    }
    return render(request, 'devtool/dev_list.html', ctx)

def devtool_detail(request):
    pass

def devtool_create(request):
    pass

def devtool_update(request):
    pass

def devtool_delete(request):
    pass