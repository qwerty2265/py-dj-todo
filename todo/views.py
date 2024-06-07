from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'completed', 'category']
    template_name = 'task_form.html'

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed', 'category']
    template_name = 'task_form.html'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'task_form.html'
