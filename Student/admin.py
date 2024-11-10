from django.contrib import admin
from .models import Department
# Register your models here.
admin.site.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dept_name','building','budget']
#
#
# d = Department()
# def total_number(d):
#     total = len(Student.)