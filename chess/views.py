from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from .forms import ReviewForm
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
    queryset = Articles.objects.order_by("-id")
    paginate_by = 7

class ArticleViews(DetailView):
    """Одна статья"""
    model = Articles
    slug_field = "slug"


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        article = Articles.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.article = article
            form.save()
        return redirect(article.get_absolute_url())
