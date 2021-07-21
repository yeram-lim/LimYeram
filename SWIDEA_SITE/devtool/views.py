from devtool.models import Devtool
from django.shortcuts import get_object_or_404, redirect, render
from .forms import DevForm

def devtool_list(request):
    all = Devtool.objects.all()
    ctx = {
        'all' : all,
    }
    return render(request, 'devtool/dev_list.html', ctx)

def devtool_detail(request, pk):
    tool = Devtool.objects.get(pk=pk)
    ctx = {
        'tool': tool,
    }
    return render(request, 'devtool/dev_detail.html', ctx)
    pass

def devtool_create(request):
    if request.method == 'POST':
        form = DevForm(request.POST)
        if form.is_valid():
            dev = form.save()
            return redirect('devtool:devtool_detail', dev.id)
    else:
        form = DevForm()
        ctx = {'form': form}
        return render(request, 'devtool/dev_form.html', ctx)

def devtool_update(request, pk):
    dev = get_object_or_404(Devtool, pk=pk)

    if request.method == 'POST':
        form = DevForm(request.POST, instance=dev)
        if form.is_valid():
            dev = form.save()
            return redirect('devtool:devtool_detail', pk)
    else:
        form = DevForm(instance=dev)
        ctx = {'form': form}
        return render(request, 'devtool/dev_form.html', ctx)

def devtool_delete(request, pk):
    dev = Devtool.objects.get(pk=pk)
    dev.delete()
    return redirect('devtool:devtool_list')