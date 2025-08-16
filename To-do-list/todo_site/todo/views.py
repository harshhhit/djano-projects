
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TodoForm
from .models import Todo


# def index(...): This defines the function. The name index is a common convention for the main page of an app, but you can name it anything you want.

# (request): This is the most important part. Django automatically passes an HttpRequest object to every view function as its first argument. This request object contains all the information about the incoming request, such as:

#     The user's method (GET, POST, etc.)

#     Any data submitted in a form

#     Information about the logged-in user

#     The requested URL path

# The body of the function: This is where you write the code to handle the request. This could be fetching data from a database, processing a form, or performing any other logic.

# The return value: A view function must return an HttpResponse object. This object contains the content to be sent back to the user's brows

def index(request):
    
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

# https://youtu.be/h05UEays2KI?embeds_referring_euri=https%3A%2F%2Fgemini.google.com%2F&source_ve_path=MTY0NTAz



def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')


# When do you use reverse_lazy?

# You typically use reverse_lazy when you want to redirect someone to another page after they do something 
# (like submit a form) in class-based views (CBVs).