from django.contrib import admin

from .models import Class, Teacher, Student

admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Student)