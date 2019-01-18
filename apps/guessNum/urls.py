from django.urls import path

from apps.guessNum import views

app_name = 'guess'


urlpatterns = [
    path('index', views.IndexVIew.as_view(), name='index')
]