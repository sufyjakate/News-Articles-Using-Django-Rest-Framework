from rest_framework import routers

from testing.views import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, base_name='source')

urlpatterns = router.urls
