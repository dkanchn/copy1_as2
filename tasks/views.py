from django.shortcuts import render

from tasks.forms import TaskForm

# Create your views here.
tasks = ["foo", "bar", "baz"]

def index(request):
    context = {
        "tasks": tasks
    }
    return render(request, "tasks/index.html", context)


def add(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            tasks.append(form.cleaned_data["task"])
            return render(request, "tasks/index.html", {"tasks": tasks})
        
    
    return render(request, "tasks/add.html", {"form": form})