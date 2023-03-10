from django.urls import include, path
from . import views
urlpatterns = [
        path('', views.index, name='index'),  # index view at /
        path('post/', views.likePost, name='likepost'),   # likepost view at /likepost
   ]