"""ghost_post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from ghost_post import views
from ghost_post.models import BoastandRoast

admin.site.register(BoastandRoast)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upvote/<int:id>', views.upvote, name='homepage'),
    path('downvote/<int:id>', views.downvote, name='homepage'),
    path('post/', views.addpost, name='post'),
    path('boast/', views.boasts_view, name='homepage'),
    path('roast/', views.roasts_view, name='homepage'),
    path('hated/', views.hated_view, name='homepage'),
    path('loved/', views.lovely_view, name='homepage'),
    path('', views.index, name='homepage'),
]
