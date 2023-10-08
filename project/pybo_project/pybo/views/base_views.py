from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from pybo.models import Class

def greet(request):
    return HttpResponse("곧 게시판으로 바뀌게 될거에여")

def class_list(request):
    page = request.GET.get('page', '1')
    class_list = Class.objects.order_by('-create_date')
    paginator = Paginator(class_list, 4)
    page_obj = paginator.get_page(page)
    context = {'class_list' : page_obj}
    return render(request, 'pybo/class_list.html', context)


def class_detail(request, class_id):
    _class = get_object_or_404(Class, id=class_id)
    context = { 'class': _class }
    return render(request, 'pybo/class_detail.html', context)