from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import DashboardView, SignupView

app_name = 'accounts'

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
