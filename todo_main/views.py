
from django.shortcuts import render
from todo.models import Task
def home(request):
    # Add starter tasks once for fresh deployments with an empty database.
    if not Task.objects.exists():
        Task.objects.bulk_create([
            Task(task='Plan your day'),
            Task(task='Complete one priority task'),
            Task(task='Review completed items', is_completed=True),
        ])

    tasks= Task.objects.filter(is_completed = False). order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed= True)

    context = {
        'tasks' : tasks,
        'completed_tasks' : completed_tasks,
    }   
    return render(request, 'home.html' , context)
