from django.urls import path, include
from .import views
app_name = 'contact'
urlpatterns = [
    path('', views.addtrainee.as_view(), name = 'view'),
    path('insert/', views.insert,name = 'save'),
    path('login/',views.login,name = 'login')
]
