import logging
import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView
from .models import Item
from .forms import ItemForm

def archives_year(requset, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')#q가 없다면 빈문자가 대신한다.
    if q: #검색어가 있다면
        qs = qs.filter(name__icontains=q)#i: 대소문자 구별x
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q, #검색창에 내가 검색한 내용이 찍히게 한다.
    })

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })

# def item_new(request, item=None):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=item) #instance=item: 이걸로 edit한다.
#         if form.is_valid():
#             item = form.save() #ModelForm에서 제공
#             return redirect(item)
#     else:
#         form = ItemForm(instance=item)

#         return render(request, 'shop/item_form.html', {
#         'form': form,
#         })

# def item_edit(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return item_new(request, item)

item_new = CreateView.as_view(model=Item, form_class=ItemForm)
item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)