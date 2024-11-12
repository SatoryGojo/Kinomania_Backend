from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    

    

class FilmModel(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    preview = models.ImageField(verbose_name='Превью', upload_to='film_preview')
    director = models.CharField(verbose_name='Режиссер', max_length=100)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'