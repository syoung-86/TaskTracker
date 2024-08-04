from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': TaskForm()})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Task created successfully'})
            else:
                return redirect('task_list')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
            else:
                return render(request, 'tasks/task_list.html', {'form': form})

    return HttpResponseBadRequest("Invalid request")


@login_required
def delete_task(request, task_id):
    if request.method == 'DELETE':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'})
    return HttpResponseBadRequest("Invalid request")


@login_required
def complete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.completed = True
        task.save()
        return JsonResponse({'message': 'Task marked as complete'})
    return HttpResponseBadRequest("Invalid request")
