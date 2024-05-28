from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse

def index(request):
    is_signed_in = request.session.pop('is_signed_in', False)
    return render(request, 'index.html', {'is_signed_in': is_signed_in})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = name
            user.save()

            # Redirect to index page after successful signup
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('index')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return redirect('signup')

    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome to TradeWise")
            request.session['is_signed_in'] = True
            return redirect('index')  # Redirect to the index view
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('signin')  # Redirect to signin page again on failure

    return render(request, 'signin.html')

def signout(request):
    return render(request, 'signout.html')

