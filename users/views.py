from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.

def logout_view(request):
    # Log out from web page
    logout(request)
    return redirect('learning_logs:index')
