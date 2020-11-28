from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from .models import Articles, Treners, Videos, Files


class IndexViews(View):
    """Список статей"""
    def get(self, request):
        articles = Articles.objects.all()
        return render(request, "chess/index.html", {"articles_list": articles})

class TrenersViews(View):
    """Список тренеров"""
    def get(self, request):
        treners = Treners.objects.all()
        return render(request, "chess/treners.html", {"treners_list": treners})

class PrsonalTreningViews(View):
    """Список тренеров"""
    def get(self, request):
        articles = Articles.objects.all()
        return render(request, "chess/personal_trening.html", {"articles_list": articles})

class VideosViews(View):
    """Список видео"""
    def get(self, request):
        videos = Videos.objects.all()
        return render(request, "chess/videos.html", {"videos_list": videos})

class FilesViews(View):
    """Список файлов"""
    def get(self, request):
        files = Files.objects.all()
        return render(request, "chess/files.html", {"files_list": files})

class ArticlesViews(ListView):
    """Список статей"""
    model = Articles
    queryset = Articles.objects.all()


class ArticleViews(DetailView):
    """Одна статья"""
    model = Articles
    slug_field = "slug"

