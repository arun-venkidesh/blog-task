from django.shortcuts import render, redirect
from blogtaskapp.forms import PoemForm
from .models import poems
# Create your views here.

def index(request):
    if request.method == "POST":
        form=PoemForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        form=PoemForm()
    return render(request,"index.html",{'form':form})

def home(request):
    detail=poems.objects.all()
    return render(request,"home.html",{'detail':detail})

def edit(request,id):
    rewrite=poems.objects.get(id=id)
    return render(request,"edit.html",{'rewrite':rewrite})

def update(request, id):
    if request.method == "POST":
        rewrite=poems.objects.get(id=id)
        print("save")
        form=PoemForm(request.POST, instance=rewrite)
        if form.is_valid():
            print("success")
            form.save()
            return redirect("/home")
    else:
        form=PoemForm(instance=rewrite)
    return render(request,'edit.html',{'rewrite':rewrite, 'form':form})

def destroy(request,id):
    rewrite=poems.objects.get(id=id)
    rewrite.delete()
    return redirect("/home")