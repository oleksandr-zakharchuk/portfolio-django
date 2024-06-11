from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from .models import Articles
from rest_framework import mixins
from .serializers import ArticlesSerializer


class ArticlesViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):

    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


def index(request):
    news = Articles.objects.all()
    row_count = (len(news) // 2) + 1
    row_count_range = range(0, row_count)
    return render(request, 'main/index.html', {'news': news, 'row_count_range': row_count_range})
