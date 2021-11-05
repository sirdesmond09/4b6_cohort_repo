from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

 
def password_is_strong(password):
    
    """Function to cehck if password is strong."""
    
    if (len(password) < 6) or (len(password)>16):
        isValid = False
    elif not any(char.isdigit() for char in password):
        isValid = False
    elif not any(char.islower() for char in password):
        isValid = False
    elif not any(char.isupper() for char in password):
        isValid = False
    else:
        isValid=True
        
    return isValid




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


def signup_view(request):
    if request.method == 'POST':
        data = {key:request.POST.get(key) for key in request.POST.keys()} #create a dictionary of the data passed by the template
        
        if 'csrfmiddlewaretoken' in data.keys():
            data.pop('csrfmiddlewaretoken') #remove the csrf token
            
        password = data.pop('password')
        re_password = data.pop('re_password')
        
        if password == re_password: #validate that both passwords are the same 
            
            if password_is_strong(password): #check that the password is strong
                data['password'] = password #if passwords are the same, add the original password to the data
                try:
                    User.objects.create(**data, is_active=False) #create the user account
                    messages.success(request,"Account created successfully")
                except Exception:
                    messages.warning(request,"Username has been taken")
            else:
                messages.warning(request,"Password length should not be less than 6")
                messages.warning(request, "Password should contain at least:\n A number\n A lowercase letter [a-z] \n A uppercase letter [A-Z]")
        else:
            messages.warning(request, 'Please enter matching passwords') #return a message if the passworods are not correct
        
        
        
    return render(request, 'registration/signup.html')