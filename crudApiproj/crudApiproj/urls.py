"""
URL configuration for crudApiproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from crudApp.views import PostListCreateView,PostRetrieveUpdateDeleteView,LikeListCreateView,LikeRetrieveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/',PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),
    path('likes/',LikeListCreateView.as_view(),name='like-list'),
    path('likes/<int:pk>/',LikeRetrieveUpdateDeleteView.as_view(),name='like-detail'),

]
