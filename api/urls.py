from rest_framework import routers

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('api',)

app_name = 'api'

urlpatterns = [
    path(),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
