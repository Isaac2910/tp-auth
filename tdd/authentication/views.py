from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login,  logout # import des fonctions login et authenticate






@login_required

def home(request):

    return render(request, 'authentication/home.html')



from . import forms

def logout_user(request):
    
    logout(request)
    return redirect('login')

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})


    