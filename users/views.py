from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect



# Create your views here.
def register(request):
    if request.method != 'POST':
        form = UserCreationForm
    else:
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()

            login(request, new_user)
            return redirect('MainApp:index')

    context = {'form':form}
    return render(request, 'registration/register.html', context)

def logout_user(request):
    logout(request)
    return render(request, 'registration/logged_out.html')