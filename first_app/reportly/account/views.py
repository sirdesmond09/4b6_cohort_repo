from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user:
            return redirect('attendance:all_books')
        else:
            messages.warning(request, 'Please enter a valid username and password')
            
        
    return render(request, 'registration/login.html')