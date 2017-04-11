from django.contrib.auth.models import User
from rest_framework import serializers
from .models import article


class ArticleSerializer(serializers.ModelSerializer):
    #AID = serializers.IntegerField(read_only=True)
    #Title = serializers.CharField(required=True, allow_blank=False)
    #Date = serializers.DateField(required=True)
    #Categories = serializers.CharField(required=True, allow_blank=False, max_length=100)
    #Summary = serializers.CharField(required=True, allow_blank=False)
    #Source = serializers.CharField(required=True, allow_blank=False)
    #Source_url = serializers.URLField(required=True)
    #Author = serializers.CharField(required=True, max_length=100)
    class Meta:
        model = article
        fields = '__all__'
    #def create(self, validated_data):
     #   return article.objects.create()