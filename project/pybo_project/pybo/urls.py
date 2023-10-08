from django.urls import path
from .views import base_views
from .views import class_views
from .views import student_views

app_name = 'pybo'

urlpatterns = [
    path('', base_views.greet),
    path('suyeon_class_list/', base_views.class_list, name = 'class_list'),
    path('suyeon_class_list/<int:class_id>/', base_views.class_detail, name = 'class_detail'),
    path('suyeon_class_list/class/register/', class_views.class_register, name='class_register'),
    path('suyeon_class_list/class/modify/<int:class_id>/', class_views.class_modify, name='class_modify'),
    path('suyeon_class_list/class/delete/<int:class_id>/', class_views.class_delete, name='class_delete'),
    path('suyeon_class_list/student/register/<int:class_id>/', student_views.student_register, name='student_register'),
    path('suyeon_class_list/student/modify/<int:student_id>/', student_views.student_modify, name='student_modify'),
    path('suyeon_class_list/student/delete/<int:student_id>', student_views.student_delete, name='student_delete'),
]
