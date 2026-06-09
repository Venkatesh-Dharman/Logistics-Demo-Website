from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.service),
    path('', views.about),
    path('', views.resource),
    path('', views.join),
    path('', views.project),
    path('', views.faq),
    path('', views.contact),    
]
