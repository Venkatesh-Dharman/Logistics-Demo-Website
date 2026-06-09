"""
URL configuration for Natural_Disaster_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Logistics import views


urlpatterns = [
    path('index.html', views.index, name='index'),
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('service.html', views.service, name='service'),
    path('resource.html', views.resource, name='resource'),
    path('join-our-team.html', views.join, name='join'),
    path('project.html', views.project, name='project'),
    path('faq.html', views.faq, name='faq'),
    path('contact.html', views.contact, name='contact'),
    
]

admin.site.site_url = '/index'
