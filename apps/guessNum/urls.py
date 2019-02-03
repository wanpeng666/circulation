from django.urls import path

from apps.guessNum import views

app_name = 'guess'


urlpatterns = [
    path('index', views.IndexVIew.as_view(), name='index'),
    path('game', views.CreateNewGameView.as_view(), name='game')
]