from django.shortcuts import render,  get_object_or_404, redirect
from . models import Person

def home(request):
    if request.method == "GET":
        tasks = Person.objects.all()

        return render(request, "cards.html", {'tasks': tasks[::-1]})

    if request.method == "POST":
        task_name = request.POST['task']
        tasks = Person.objects.all()
        if len(task_name) ==0: return render(request, "cards.html", {'tasks': tasks[::-1]})

        Person.objects.create(task=task_name)
        
        return render(request, "cards.html", {'tasks': tasks[::-1]})

def delete_task(request, task_id):
    tasks = Person.objects.all()
    task = get_object_or_404(Person, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, "cards.html", {'tasks': tasks[::-1]})


    



