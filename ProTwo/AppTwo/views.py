from django.shortcuts import render
from AppTwo.forms import NewUserForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    form=NewUserForm()
    if request.method == "POST":
        form=NewUserForm(request.POST)

        if form.is_valid():

            form.save(commit = True)
            return index(request)
        else:
            print('Error Form Invalid')

    return render(request,'appTwo/users.html',{'form':form})
