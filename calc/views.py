from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList

def index(response,id):
    ls=ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        #{"save":["save"],"c1":["clicked"]}
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):#we will do this to see if item is complete or not
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id))== "clicked":
                        item.complete=True
                    else:
                        item.complete=False
                    item.save()

            elif response.POST.get("newItem"):#we will get the text of the new item on to do list
                txt= response.POST.get("new")
                #now we will check if item is valid before adding it
                
                if len(txt)>2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid input")

        #item=ls.item_set.get(id=1)
        return render(response,"calc/list.html",{"ls":ls})#this means name corresponds to ls.name
    return render(response,"calc/view.html",{})
#{"name":ls.name} was written in {}
# Create your views here.

def home(response):
    return render(response,"calc/home.html",{})

#{"name": "test"} was written

def create(response):#response means post request
    if response.method == "POST":
        form=CreateNewList(response.POST)#response.POST holds all the info from our form
        if form.is_valid():#FORM class function
            n= form.cleaned_data["name"]#form takes all data from response.POST
            #cleaned_data means it will clean the data, unencrypt it
            t= ToDoList(name=n)
            t.save()#now every time a name is entered, a new todolist is created
            response.user.todolist.add(t)  # adds the to do list to the current logged in user
            
            #we used the above code previously to store all lists, but now we'll link to specific users
	        
        return HttpResponseRedirect("/%i" %t.id)  #to print the list after saving it from form

    else:  
        form=CreateNewList()#creates a blank form and passes into html {}--> check these belowe
    return render(response,"calc/create.html",{"form":form})

def view(response):
    return render(response, "calc/view.html",{})