from django.contrib import admin
from .models import UserAccountProfile

# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserAccountProfile
    can_delete = False
