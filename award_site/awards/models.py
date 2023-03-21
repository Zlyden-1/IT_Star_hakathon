from django.db import models


class Award(models.Model):
    name = models.TextField(db_index=True, verbose_name='Наименование')
    picture = models.ImageField(upload_to='pictures', verbose_name='Изображение награды')
    description = models.TextField(verbose_name='Описание награды')
    conditions = models.TextField(verbose_name='Условия получения награды')
    necessary_awards = models.TextField(verbose_name='Необходимые награды')
    excluding_awards = models.TextField(verbose_name='Запрещающие награды')
    entry = models.FileField(upload_to='entryes', verbose_name='Заявка на получение награды')
    rank = models.IntegerField(verbose_name='Степень ордена')
    necessary_docs = models.FileField(null=True, blank=True, upload_to='docs', default=None,
                                      verbose_name='Заявка на получение награды')

    def __str__(self):
        return f'{self.name}'