from django.db import models
from django.utils import timezone

from core.models import User




class GoalCategory(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(verbose_name='Название', max_length=255)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name='Удалена', default=False)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)


class Goal(models.Model):
    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    class Status(models.IntegerChoices):
        to_do = 1, "К выполнению"
        in_progress = 2, "В процессе"
        done = 3, "Выполнено"
        archived = 4, "Архив"

    class Priority(models.IntegerChoices):
        low = 1, "Низкий"
        medium = 2, "Средний"
        high = 3, "Высокий"
        critical = 4, "Критический"

    title = models.CharField(verbose_name='Название', max_length=255)
    status = models.PositiveSmallIntegerField(
        verbose_name='Статус', choices=Status.choices, default=Status.to_do
    )
    priority = models.PositiveSmallIntegerField(
        verbose_name='Приоритет', choices=Priority.choices, default=Priority.medium
    )
    due_date = models.DateField(verbose_name='Дата дедлайна')
    category = models.ForeignKey(GoalCategory, verbose_name='Категория', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)


class GoalComment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'


    text = models.TextField(verbose_name='Текст')
    goal = models.ForeignKey(
        Goal,
        verbose_name='Цель',
        on_delete=models.PROTECT,
        related_name='comments',
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.PROTECT,
        related_name='comments',
    )
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)
