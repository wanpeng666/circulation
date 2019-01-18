from django.urls import path

from apps.mast import views

app_name = 'mast'

urlpatterns = [
    path('incidents', views.incidentsView.as_view(), name='incidents'),
    path('incident/<int:id>', views.incidentDetailView.as_view(), name='incident'),
    path('test', views.testView.as_view(), name='test'),
    path('celeryTest/<int:id>', views.CeleryTest.as_view(), name='celeryTest')
]
