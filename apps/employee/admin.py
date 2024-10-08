from .models import (
    Employee,
    Status,
    Position,
    Department,
)
from django.contrib import admin

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'is_manager', 'status', 'position', 'department')
    search_fields = ('name', 'address')
    list_filter = ('status', 'position', 'department')
    
    def is_manager(self, obj):
            return obj.is_manager
    is_manager.boolean = True
    is_manager.short_description = 'is from employee health'

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary')
    search_fields = ('name',)
    list_filter = ('salary',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')
    search_fields = ('name',)
    list_filter = ('manager',)
    
    
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Department, DepartmentAdmin)
