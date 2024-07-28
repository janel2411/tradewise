from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
import re
from django.core.exceptions import ValidationError


def index(request):
    is_signed_in = request.session.pop('is_signed_in', False)
    return render(request, 'index.html', {'is_signed_in': is_signed_in})


def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not re.search(r"[A-Za-z]", password):
        raise ValidationError("Password must contain at least one letter.")
    if not re.search(r"[0-9]", password):
        raise ValidationError("Password must contain at least one number.")
    if not re.search(r"[!@#$%^&*]", password):
        raise ValidationError("Password must contain at least one special character.")

def validate_username(username):
    if not re.match(r"^(?=.*[A-Za-z])(?=.*[0-9])[A-Za-z0-9]+$", username):
        raise ValidationError("Username must contain letters and numbers.")


from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        error_messages = []

        # Email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            error_messages.append("Invalid email address.")

        # Username validation
        try:
            validate_username(username)
        except ValidationError as e:
            error_messages.append(str(e))

        # Password validation
        try:
            validate_password(password)
        except ValidationError as e:
            error_messages.append(str(e))

        if error_messages:
            for message in error_messages:
                messages.error(request, message)
            return redirect('signup')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('index')
        except Exception as e:
            messages.error(request, "Error creating account: " + str(e))
            return redirect('signup')

    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Bad Credentials! Log In Again.")
            return redirect('index')

    return render(request, 'index.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully.")
    return redirect('index')


def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'dashboard.html', context)

def lesson1(request):
    return render(request, 'lesson1.html')

def lesson2(request):
    return render(request, 'lesson2.html')

def lesson3(request):
    return render(request, 'lesson3.html')

def lesson4(request):
    return render(request, 'lesson4.html')

@login_required
def start_chapter(request):
    user_profile = request.user.profile
    completed_lessons = user_profile.completed_lessons

    lessons = ['lesson1', 'lesson2', 'lesson3', 'lesson4']
    next_lesson = None

    for lesson in lessons:
        if lesson not in completed_lessons:
            next_lesson = lesson
            break

    if next_lesson:
        return redirect(next_lesson)
    else:
        return redirect('dashboard')
    
@login_required
def complete_lesson(request, lesson_id):
    if request.method == 'POST':
        user_profile = request.user.profile

        # Update points
        user_profile.points += 5

        # Mark lesson as completed
        if lesson_id not in user_profile.completed_lessons:
            user_profile.completed_lessons.append(lesson_id)
        
        user_profile.save()

        return JsonResponse({'success': True, 'points': user_profile.points})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

from django.http import JsonResponse
from .models import Profile

def updatepoints(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.points += 5
        profile.save()
        return JsonResponse({'success': True, 'points': profile.points})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

from django.shortcuts import render

def react_app(request):
    return render(request, 'quiz.html')

def quizhomepage(request):
    return render(request, 'quizhomepage.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment, Profile
from .forms import PostForm, CommentForm, ReplyForm

# Home page for the forum
def forumhomepage(request):
    categories = Category.objects.all()
    return render(request, 'forumhomepage.html', {'categories': categories})

# View for category detail which lists posts in that category
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    return render(request, 'category_detail.html', {'category': category, 'posts': posts})

# View for post detail which shows the post and its comments
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(parent=None).order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user.profile
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

# View to create a new post
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    categories = Category.objects.all()
    return render(request, 'post_edit.html', {'form': form, 'categories': categories, 'post': None})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    categories = Category.objects.all()
    return render(request, 'post_edit.html', {'form': form, 'categories': categories, 'post': post})


# View to add a new comment
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.profile
            comment.save()
            return redirect('post_detail', pk=post.pk)
    return redirect('post_detail', pk=post.pk)

# View to add a reply to an existing comment
@login_required
def add_reply(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.post
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.comment = comment
            reply.author = request.user.profile
            reply.save()
            return redirect('post_detail', pk=post.pk)
    else:
        reply_form = ReplyForm()
    return render(request, 'post_detail.html', {'post': post, 'reply_form': reply_form, 'comment': comment})

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def leaderboard(request):
    # Get the top 5 ranks
    top_users = list(Profile.objects.all().order_by('-points', 'username'))
    top_users_filtered = []
    last_points = None
    rank_count = 0

    for user in top_users:
        if len(top_users_filtered) < 5 or (last_points is not None and user.points == last_points):
            top_users_filtered.append(user)
            last_points = user.points
            rank_count = len(top_users_filtered)

    top_users_data = [{"username": user.username, "points": user.points, "first_name": user.first_name, "last_name": user.last_name} for user in top_users_filtered]
    
    current_user = request.user
    current_user_profile = Profile.objects.get(user=current_user)
    current_user_data = {
        "username": current_user.username,
        "points": current_user_profile.points,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name
    }
    
    return JsonResponse({"top_users": top_users_data, "current_user": current_user_data})

import requests
from django.shortcuts import render
from django.conf import settings
import logging

# Set up logging
logger = logging.getLogger(__name__)

def fetch_market_news(request):
    tickers = [
        "eurusd", "usdjpy", "gbpusd", "usdchf", "audusd", "usdcad", "nzdusd"
    ]
    data = []

    url_template = "https://api.tiingo.com/tiingo/fx/{}/top"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {settings.TIINGO_API_TOKEN}'
    }

    for ticker in tickers:
        url = url_template.format(ticker)
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            json_response = response.json()
            if json_response:  # Check if the response is not empty
                data.append({
                    "ticker": ticker,
                    "bidPrice": json_response[0].get('bidPrice', 'N/A'),
                    "askPrice": json_response[0].get('askPrice', 'N/A')
                })
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch data for {ticker}: {e}")
            data.append({
                "ticker": ticker,
                "bidPrice": 'N/A',
                "askPrice": 'N/A'
            })

    return render(request, 'market_news.html', {'market_data': data})
