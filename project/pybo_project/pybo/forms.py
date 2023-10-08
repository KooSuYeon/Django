from django import forms
from pybo.models import Class, Student

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['subject', 'class_info']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'class_info': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
        }
        labels = {
            'subject' : "강의명", 
            'class_info' : '강의 정보',
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_code']
        widgets = {
            'student_code' : forms.TextInput(attrs={'class': 'form-control', 'rows': 2})
        }
        labels = {
            'student_code': '학생 학번',
        }