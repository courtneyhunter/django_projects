from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.MainView.as_view(), name='athletes'),
    path('main/create/', views.AthleteCreate.as_view(), name='athlete_create'),
    path('main/<int:pk>/update/', views.AthleteUpdate.as_view(), name='athlete_update'),
    path('main/<int:pk>/delete/', views.AthleteDelete.as_view(), name='athlete_delete'),
    path('lookup/', views.SportView.as_view(), name='sport_list'),
    path('lookup/create/', views.SportCreate.as_view(), name='sport_create'),
    path('lookup/<int:pk>/update/', views.SportUpdate.as_view(), name='sport_update'),
    path('lookup/<int:pk>/delete/', views.SportDelete.as_view(), name='sport_delete'),
]
