from django.urls import path

from apps.mast import views

app_name = 'mast'

urlpatterns = [
    path('incidents', views.incidentsView.as_view(), name='incidents'),
    path('incident/<int:id>', views.incidentDetailView.as_view(), name='incident'),
]
