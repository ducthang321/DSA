from django.contrib.auth import views as auth_views
from django.urls import include, path
from .import views
app_name = 'Usermember'
urlpatterns = [
    path('',views.loginUser.as_view(), name='loginUser' ),
    path('logout/', views.logoutUser, name='logoutUser' ),
    path('register.html', views.registerUser.as_view(), name='registerUser' ), 
]