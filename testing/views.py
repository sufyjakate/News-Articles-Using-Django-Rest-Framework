# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import article
from .serializers import ArticleSerializer
import django_filters
from rest_framework import generics

#import json
#def get_json():
#    file_open = open('/Users/sufyjakate/PycharmProjects/django_test1/testing/fixtures/master.json', 'r')
#    json_data = json.loads(file_open)
#    return Response(json_data)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Date', 'Categories', 'Source')

    #def get_queryset(self):
    #    queryset = article.objects.all()
    #    source = self.request.query_params.get('source', None)
    #    if source is not None:
    #        queryset = queryset.filter(Source=source)
    #    return queryset

