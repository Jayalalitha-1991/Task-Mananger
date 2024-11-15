# from django.shortcuts import render

# # Create your views here.
# # tasks/views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Task
# from .forms import TaskForm

# @login_required
# def task_list(request):
#     tasks = Task.objects.filter(user=request.user)
#     priority_filter = request.GET.get('priority')
#     if priority_filter:
#         tasks = tasks.filter(priority=priority_filter)
#     return render(request, 'tasks/task_list.html', {'tasks': tasks})

# @login_required
# def task_create(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.user = request.user
#             task.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()
#     return render(request, 'tasks/task_form.html', {'form': form})


# @login_required
# def task_edit(request, pk):
#     task = get_object_or_404(Task, pk=pk, user=request.user)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm(instance=task)
#     return render(request, 'tasks/task_form.html', {'form': form})

# @login_required
# def task_delete(request, pk):
#     task = get_object_or_404(Task, pk=pk, user=request.user)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('task_list')
#     return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_all_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'add_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('view_all_tasks')

def view_all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'view_all_tasks.html', {'tasks': tasks})

def filter_tasks_by_priority(request, priority):
    tasks = Task.objects.filter(priority=priority)
    return render(request, 'view_all_tasks.html', {'tasks': tasks})
