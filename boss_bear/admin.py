from django.contrib import admin

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'id_card_number',
        'mobile_number',
        'sex',
        'nationality'
    ]

admin.site.register(Employee, EmployeeAdmin)
