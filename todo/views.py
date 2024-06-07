from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Category

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        category_name = self.request.get()
        if category_name:
            context = Task.objects.filter(category=category_name)
            
        return context
    
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

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'
    template_name = 'category_form.html'
    