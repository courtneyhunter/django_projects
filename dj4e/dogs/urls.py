from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.DogList.as_view(), name='dogs'),
    path('main/create/', views.DogCreate.as_view(), name='dog_create'),
    path('main/<int:pk>/update/', views.DogUpdate.as_view(), name='dog_update'),
    path('main/<int:pk>/delete/', views.DogDelete.as_view(), name='dog_delete'),
    path('lookup/', views.TypeView.as_view(), name='type_list'),
    path('lookup/create/', views.TypeCreate.as_view(), name='type_create'),
    path('lookup/<int:pk>/update/', views.TypeUpdate.as_view(), name='type_update'),
    path('lookup/<int:pk>/delete/', views.TypeDelete.as_view(), name='type_delete'),
]
