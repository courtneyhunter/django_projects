from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.FruitListView.as_view()),
    path('fruits', views.FruitListView.as_view(), name='fruits'),
    path('fruit/<int:pk>', views.FruitDetailView.as_view(), name='fruit_detail'),
    path('fruit/create', views.FruitFormView.as_view(success_url=reverse_lazy('fruits')), name='fruit_create'),
    path('fruit/<int:pk>/update', views.FruitFormView.as_view(success_url=reverse_lazy('fruits')), name='fruit_update'),
    path('fruit/<int:pk>/delete', views.FruitDeleteView.as_view(success_url=reverse_lazy('fruits')), name='fruit_delete'),
    path('fruit/<int:pk>/comment', views.CommentCreateView.as_view(), name='fruit_comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(success_url=reverse_lazy('fruits')), name='fruit_comment_delete'),
    # path('fruit/<int:pk>/favorite', views.AddFavoriteView.as_view(), name='fruit_favorite'),
    # path('fruit/<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='fruit_unfavorite'),
]
