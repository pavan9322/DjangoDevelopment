from django.shortcuts import render
from django.http import HttpResponse
from .models import Reg
from .forms import LoginForm
from .forms import RegForm
def reg(request):
        if request.method == 'POST':
         form = RegForm(request.POST)
         if form.is_valid():
            form.save(commit=True)
            return HttpResponse('reg success')
         else:
            print(form.errors)
            return HttpResponse("error")
        else:
          form = RegForm()
          return render(request,'reg.html', {'form': form})
def login(request):
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            un =MyLoginForm.cleaned_data['user']
            pw=MyLoginForm.cleaned_data['pwd']
            dbuser = Reg.objects.filter(user=un,pwd=pw)
            if not dbuser:
                return HttpResponse('login faild')
            else:
                return HttpResponse('login success')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
def home(request):
    return render(request,'home.html')
