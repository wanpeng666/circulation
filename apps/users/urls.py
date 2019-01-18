from django.urls import path

from apps.users import views

app_name = 'user'


urlpatterns = [
    path('login', views.LoginView.as_view(), name='login')
]