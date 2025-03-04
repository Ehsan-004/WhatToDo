from django.contrib import admin
from .models import Task, SubTask



class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'status', 'priority')
    search_fields = ('create_date', 'name') 
    list_filter = ('create_date', 'deadline_date') 
    
    
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_task')
    
    
admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)

