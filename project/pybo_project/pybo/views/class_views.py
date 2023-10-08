from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages

from pybo.models import Class
from pybo.forms import ClassForm


@login_required(login_url='common:login')
def class_register(request):
    # 등록 버튼을 눌렀을 때에는 POST 방식으로 호출된다.
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            _class = form.save(commit=False)
            # 글쓴이 항목 추가
            _class.professor = request.user
            _class.create_date = timezone.now()
            _class.save()
            return redirect('pybo:class_list')
    else:
        form = ClassForm()
    context = {'form' : form}
    return render(request, 'pybo/class_register_form.html', context)


@login_required(login_url='common:login')
def class_modify(request, class_id):
    _class = get_object_or_404(Class, pk=class_id)
    if request.user != _class.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:class_detail', class_id = _class.id)
    if request.method == "POST":
        form = ClassForm(request.POST, instance = _class)
        if form.is_valid():
            _class = form.save(commit=False)
            _class.modify_date = timezone.now()
            _class.save()
            return redirect('pybo:class_detail', class_id = _class.id)
        
    # 수정 버튼을 눌렀을 떄 GET 방식으로 호출된다.
    else:
        form = ClassForm(instance=_class)
    context = {'form' : form}
    return render(request, 'pybo/class_register_form.html', context)


@login_required(login_url='common:login')
def class_delete(request, class_id):
    _class = get_object_or_404(Class, pk=class_id)
    if request.user != _class.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:class_detail', class_id=_class.id)
    _class.delete()
    return redirect('pybo:class_list')
    