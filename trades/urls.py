from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('lesson1/', lesson1, name='lesson1'),
    path('lesson2/', lesson2, name='lesson2'),
    path('lesson3/', lesson3, name='lesson3'),
    path('lesson4/', lesson4, name='lesson4'),
    path('updatepoints/', updatepoints, name='updatepoints'),
    path('quiz/', react_app, name='react_app'),
    path('quizhomepage/', quizhomepage, name='quizhomepage'),
    path('forum/', forumhomepage, name='forumhomepage'),
    path('forum/category/<int:category_id>/', category_detail, name='category_detail'),
    path('forum/post/<int:pk>/', post_detail, name='post_detail'),
    path('forum/post/new/', post_new, name='post_new'),
    path('forum/post/edit/<int:post_id>/', edit_post, name='edit_post'),
    path('forum/post/<int:post_id>/add_comment/', add_comment, name='add_comment'),
    path('forum/comment/<int:comment_id>/add_reply/', add_reply, name='add_reply'),
    path('api/leaderboard/', leaderboard, name='api_leaderboard'),
    path('leaderboard/', TemplateView.as_view(template_name='leaderboard.html'), name='leaderboard'),
    path('start_chapter/', start_chapter, name='start_chapter'),
    path('complete_lesson/<str:lesson_id>/', complete_lesson, name='complete_lesson'),
]
