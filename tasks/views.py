from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': TaskForm()})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Task created successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseBadRequest("Invalid request")


def delete_task(request, task_id):
    if request.method == 'DELETE':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'})
    return HttpResponseBadRequest("Invalid request")
