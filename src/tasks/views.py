from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskCreateForm
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "tasks/task_list.html", context)


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
        else:
            return render(request, "tasks/create_task.html", {"form": form})
    else:
        form = TaskCreateForm()
    context = {"form": form}
    return render(request, "tasks/create_task.html", context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("task_list")
