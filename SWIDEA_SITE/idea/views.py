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

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES) #, instance=idea 이따가 추가해보기
        if form.is_valid():
            idea = form.save() #ModelForm에서 제공
            return redirect('idea:idea_detail', idea.id)
    else:
        form = IdeaForm()#instance=idea
        ctx = {'form': form}
        return render(request, 'idea/form.html', context=ctx)
    
def idea_update(request, pk):
    idea = get_object_or_404(IdeaList, pk=pk)

    if request.method == 'POST':
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect('idea:idea_detail', pk)
    else:
        form = IdeaForm(instance=idea)
        ctx = {'form': form }

        return render(request, 'idea/form.html', context=ctx)

def idea_delete(request, pk):
    idea = IdeaList.objects.get(pk=pk)
    idea.delete()
    return redirect('idea:idea_list')