from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

def home(request):
    # je code hier
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account is succesvol aangemaakt. Je kunt nu inloggen.')
            return redirect('login')
        
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

