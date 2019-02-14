"""bakers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from recipes.views import RecipeIndexView
from . import views

app_name = 'bakers'
urlpatterns = [
    # /admin/
    path('admin/', admin.site.urls),
    # /recipes/
    path('recipes/', include('recipes.urls')),
    path('', RecipeIndexView.as_view()),
    # /users/
    path('baker/', include('users.urls')),
    # /login/
    path('login/', LoginView.as_view(), name='login'),
    # /logout/
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    # /signup/
    path('signup/', views.Registration.as_view(), name='registration'),
]
