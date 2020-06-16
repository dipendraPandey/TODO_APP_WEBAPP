from django.db import models
from django.utils import timezone

# Create your models here.

class TaskModel(models.Model):
	title = models.CharField(max_length=30, null=True, blank=False)
	completed = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_completed = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.title

	def save(self, *arg, **kwargs):
		if self.completed :
			self.date_completed = timezone.now()
		else:
			self.date_completed = None
		super(TaskModel, self).save(*arg, **kwargs) 

	class Meta:
		verbose_name = 'Task'
		verbose_name_plural = 'Tasks'