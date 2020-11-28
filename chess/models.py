from django.db import models
from django.contrib.auth.models import User


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

# class Comments(models.Model):
#     """Коментарии"""
#     name = models.CharField("Идентефикатор", max_length=1024)
#
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Комментарий"
#         verbose_name_plural = "Комментарии"
