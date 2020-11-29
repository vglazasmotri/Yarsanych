from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from .forms import ReviewForm
from .models import Articles, Treners, Videos, Files, Index, Trenings


class IndexViews(View):
    """Главная страница"""

    def get(self, request):
        article = Index.objects.all()
        return render(request, "chess/index.html", {"articles_list": article})


class PrsonalTreningViews(View):
    """Персональные тренировки"""

    def get(self, request):
        article = Trenings.objects.all()
        return render(request, "chess/personal_trening.html", {"articles_list": article})


class TrenersViews(ListView):
    """Список тренеров"""
    model = Treners
    queryset = Treners.objects.all()
    paginate_by = 7


class VideosViews(ListView):
    """Список видео"""
    model = Videos
    queryset = Videos.objects.order_by("-id")
    paginate_by = 7


class FilesViews(ListView):
    """Список файлов"""
    model = Files
    queryset = Files.objects.order_by("-id")
    paginate_by = 7


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
