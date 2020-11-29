from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Articles(models.Model):
    """Статьи"""
    title = models.CharField("Название", max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    intro_text = models.TextField("Короткое описание", blank=True)
    full_text = models.TextField("Текст", blank=True, db_index=True)
    img = models.ImageField("Изображение", upload_to="img/chess/", blank=True)
    author = models.CharField("Автор", max_length=150, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    buyers = models.ManyToManyField(User, verbose_name="Покупатели", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_url", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Files(models.Model):
    """Файлы"""
    title = models.CharField("Название", max_length=1024)
    description = models.TextField("Описание")
    img = models.ImageField("Изображение", upload_to="img/files/")
    price = models.PositiveIntegerField("Цена", default=0)
    file = models.FileField("Файл", upload_to="files/")
    buyers = models.ManyToManyField(User, verbose_name="Покупатели", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


class Videos(models.Model):
    """Видео"""
    title = models.CharField("Название", max_length=1024)
    description = models.TextField("Описание")
    img = models.ImageField("Изображение", upload_to="img/files/")
    price = models.PositiveIntegerField("Цена", default=0)
    video = models.FileField("Файл", upload_to="videos/")
    buyers = models.ManyToManyField(User, verbose_name="Покупатели", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"


# class Pokupateli(models.Model):
#     """Покупатели"""
#     name = models.CharField("Идентефикатор", max_length=1024)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Покупатель"
#         verbose_name_plural = "Покупатели"

class Treners(models.Model):
    """Тренеры"""
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    img = models.ImageField("Изображение", upload_to="img/treners/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    article = models.ForeignKey(Articles, verbose_name="Статья", on_delete=models.CASCADE)
    checked = models.BooleanField("Проверено", default=False)

    def __str__(self):
        return f"{self.name} - {self.article}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"