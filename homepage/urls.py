from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomepageView

app_name = 'homepage'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomepageView.as_view(), name='homepage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
