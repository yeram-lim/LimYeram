from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import IdeaList
from .forms import IdeaForm

def idea_list(request):
    all_list = IdeaList.objects.all()
    ctx = { #데이터를 플레이팅
        "all_list": all_list,
    }
    return render(request, "idea/list.html", ctx)

def idea_detail(request, pk):
    idea = IdeaList.objects.get(pk=pk)
    ctx = {
        "idea": idea,
    }
    return render(request, "idea/detail.html", ctx)

def idea_create(request, idea=None):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea) 
        if form.is_valid():
            item = form.save() #ModelForm에서 제공
            return redirect(item)
    else:
        form = IdeaForm(instance=idea)

        return render(request, 'idea/form.html', {
            'form': form,
        })
    
