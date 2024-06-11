from datetime import datetime

from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Announcement', max_length=250)
    full_text = models.TextField('Article')
    created_date = models.DateTimeField('Creation date', default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
