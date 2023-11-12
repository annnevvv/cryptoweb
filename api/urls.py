from rest_framework import routers

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import CryptocurrencyExchangeViewSet

router = routers.DefaultRouter()
router.register('crypto_exchange', CryptocurrencyExchangeViewSet)

app_name = 'api'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls), name= 'rest')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
