from django.contrib import admin

# Register your models here.

from employee.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    fieldsets= [
        ('Employee',{'fields': ['name','birthDay','homeTown','phone', 'gender','educationLevel', 'avatar']}),
    ]

admin.site.register(Employee, EmployeeAdmin)