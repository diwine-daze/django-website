from django.shortcuts import redirect, render
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method =="POST": #means we are creating a new user
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()#this saves the new user in the database
        return redirect("/home")
    else:#create a blank form if we don't get a post response
        form=RegisterForm()
    return render(response, "register/register.html", {"form":form})

