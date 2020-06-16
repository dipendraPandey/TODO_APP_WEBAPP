from django.contrib import admin
from .models import TaskModel
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
	list_display = ['title', 'completed', 'date_created']
	list_filter = ('completed', 'date_created')
	search_fields = ('title','date_created')


admin.site.register(TaskModel, TaskAdmin)