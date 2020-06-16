from django.urls import path 
from task.views import task_list_view




app_name = 'task'


urlpatterns = [
		path('', task_list_view, name = 'task_list'),

]