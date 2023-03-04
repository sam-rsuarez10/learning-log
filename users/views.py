from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
    # Log out from web page
    logout(request)
    return redirect('learning_logs:index')

def register(request):
    """ Register a new user """
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user and then redirect to home page
            authenticated_user = authenticate(username=new_user, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('learning_logs:index')
    
    return render(request, 'users/register.html', {'form': form})
