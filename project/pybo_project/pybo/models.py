from django.db import models
from django.contrib.auth.models import User

class Class(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    class_info = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Student(models.Model):
    # 모델의 속성 값을 주의해서 작성하자...
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    student_code = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

