from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('mitigate/<int:finding_id>/', views.mitigate_finding, name='mitigate_finding'),
]