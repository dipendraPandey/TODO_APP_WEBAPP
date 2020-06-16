from django.shortcuts import render, redirect,  get_object_or_404
from task.models import TaskModel
from .forms import TaskForm
import json 
# Create your views here.
def task_list_view(request):
	tasks = TaskModel.objects.all()[::-1]
	contents = {'tasks':tasks}
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			if request.POST.get('id'):
				id = request.POST.get('id')
				task = TaskModel.objects.get(id=id)
				task.completed = form.cleaned_data['completed']
				task.save()
				return redirect('task:task_list')
			else:
				form.save()
			contents['Message']=' Todo Task Created'
			return redirect('task:task_list')
		return redirect('task:task_list')
	elif request.method =='DELETE':
		id = json.loads(request.body)['id']
		task = get_object_or_404(TaskModel, id=id)
		task.delete()
		return redirect('task:task_list')


	return render(request, 'task/list.html', contents)



