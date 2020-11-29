from django.urls import path

from . import views


urlpatterns = [
    path("", views.IndexViews.as_view(), name='index_url'),
    path("trenery/", views.TrenersViews.as_view(), name='treners_url'),
    path("zanytiya/", views.PrsonalTreningViews.as_view(), name='prsonal_trening_url'),
    path("video/", views.VideosViews.as_view(), name='videos_url'),
    path("file/", views.FilesViews.as_view(), name='files_url'),
    path("novosti/", views.ArticlesViews.as_view(), name='articles_list_url'),
    path("novosti/<str:slug>/", views.ArticleViews.as_view(), name='article_url'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]






