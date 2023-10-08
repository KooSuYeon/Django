from django.contrib import admin
from .models import Class

class ClassAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Class, ClassAdmin)
