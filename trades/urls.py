from django.urls import path
from .views import *

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
    path('quizhomepage/',quizhomepage,name = "quizhomepage"),
    path('forum/', post_list, name='post_list'),
    path('forum/post/<int:pk>/', post_detail, name='post_detail'),
    path('forum/post/new/', post_new, name='post_new'),

]
