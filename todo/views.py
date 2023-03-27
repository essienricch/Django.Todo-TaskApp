from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from todo.models import Task


# Create your views here.


def homepage(request):
    return render(request, 'todo/index.html')


# def view_all_tasks(request):
#     all_tasks = models.Task.objects.all()
#     return render(request, 'todo/viewall.html', {'tasks': all_tasks})

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/viewall.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'todo/create.html'
    fields = ['title', 'description', 'user', 'due_date']
    success_url = reverse_lazy('todo:task_views')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'todo/update.html'
    context_object_name = 'task'
    fields = ['title', 'description', 'task_status', 'due_date']
    success_url = reverse_lazy('todo:task_views')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/detailview.html'
    context_object_name = 'task'
    fields = ['title', 'description', 'due_date', 'task_status']


class TaskDeleteView(DeleteView):
    model = Task
    field = ['title']
    template_name = 'todo/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('todo:task_views')


def contact_us(request):
    return render(request, 'todo/contactus.html')
