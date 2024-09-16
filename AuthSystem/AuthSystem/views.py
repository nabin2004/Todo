from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task 

def home(request):
    return render(request, 'index.html')

def show(request):
    tasks = Task.objects.all()
    return render(request, 'show.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'  # Handle checkbox input

        # Basic validation
        if not title or not description:
            messages.error(request, "Both title and description are required.")
            return render(request, 'add_task.html')

        # Create the task
        Task.objects.create(title=title, description=description, completed=completed)
        
        messages.success(request, "Task added successfully!")
        return redirect('index')

    return render(request, 'add_task.html')