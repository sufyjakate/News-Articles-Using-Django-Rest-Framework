from django.conf.urls import url, include
from rest_framework import routers
from testing.views import ArticleViewSet
from django.core.urlresolvers import reverse


router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, base_name='source')

urlpatterns = router.urls