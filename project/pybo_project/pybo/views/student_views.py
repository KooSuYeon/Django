from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from pybo.models import Class, Student
from pybo.forms import StudentForm

from django.contrib.auth.decorators import login_required


def student_register(request, class_id):
    _class = get_object_or_404(Class, pk=class_id)
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.create_date = timezone.now()
            student._class = _class
            student.save()
            return redirect('pybo:class_detail', class_id = _class.id)
    else:
        form = StudentForm()
    context = {'class' : _class, 'form':form}
    return render(request, 'pybo/student_register_form.html', context)

@login_required(login_url='common:login')
def student_modify(request, student_id):
    student = get_object_or_404(Student, pk = student_id)

    if request.user != student._class.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:class_detail', class_id = student._class.id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            student = form.save(commit=False)
            student.modify_date = timezone.now()
            student.save()
            return redirect('pybo:class_detail', class_id = student._class.id)
    else:
        form = StudentForm(instance = student)
    context = {'student' : student, 'form' : form}
    # 질문과는 다르게 폼을 새로 생성해줌.
    return render(request, 'pybo/student_register_form.html', context)

@login_required(login_url='common:login')
def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.user != student._class.author:
        messages.error(request, "수정권한이 없습니다.")
    else:
        student.delete()
    return redirect('pybo:class_detail', class_id = student._class.id)