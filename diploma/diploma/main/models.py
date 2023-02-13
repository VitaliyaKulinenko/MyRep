from django.db import models
from django.urls import reverse


class Timetable(models.Model):
    days_of_the_week = models.CharField('Дни недели', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return f'{self.days_of_the_week}'

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"


class Blog(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"


class Registration(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=300)
    is_admin = models.BooleanField(default=False)

    def __repr__(self):
        return f'{self.user_name}'


class Reviews(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"









    # def get_absolute_url(self):
    #     return reverse('post', kwargs={post_id}:self.pk})

