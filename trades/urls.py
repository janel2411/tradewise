from django.urls import path
from .views import index, signup, signin, signout, dashboard, lesson1, lesson2, lesson3, lesson4,updatepoints,quiz

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

]
