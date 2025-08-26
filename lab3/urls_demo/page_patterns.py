from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.history),
    path('edit/', views.edit),
    path('discuss/', views.discuss),
    path('permissions/', views.permissions),
]
