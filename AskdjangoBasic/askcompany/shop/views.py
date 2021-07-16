from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

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

