# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

def index(request):
    is_signed_in = request.session.pop('is_signed_in', False)
    return render(request, 'index.html', {'is_signed_in': is_signed_in})

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Profile

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()         
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('index')
        except Exception as e:
            messages.error(request, "Error creating account")
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
            return redirect('index')  #redirect to index page
        else:
            messages.error(request, "Bad Credentials! Log In Again.")
            return redirect('index') #prompted to sign in again if key in wrong pw/username

    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully.")
    return redirect('index')

def dashboard(request):
    #make sure user is authenticated first
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'dashboard.html')

def lesson1(request):
    return render(request, 'lesson1.html')

def lesson2(request):
    return render(request, 'lesson2.html')

def lesson3(request):
    return render(request, 'lesson3.html')

def lesson4(request):
    return render(request, 'lesson4.html')

from django.http import JsonResponse
from .models import Profile

def updatepoints(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.points += 100
        profile.save()
        return JsonResponse({'success': True, 'points': profile.points})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

from django.shortcuts import render

def react_app(request):
    return render(request, 'quiz.html')

def quizhomepage(request):
    return render(request, 'quizhomepage.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})