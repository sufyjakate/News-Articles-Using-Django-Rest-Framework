from rest_framework import serializers

from .models import article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = '__all__'
