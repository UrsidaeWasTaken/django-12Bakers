from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'recipes'
urlpatterns = [
    # /recipes/
    path('', views.RecipeIndexView.as_view(), name='index'),

    # /recipes/<pk>/<slug>
    path('<pk>/<slug:slug>', views.RecipeDetailView.as_view(), name='detail'),

    # /recipes/create/
    path('create/', views.RecipeCreate.as_view(), name='create'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
