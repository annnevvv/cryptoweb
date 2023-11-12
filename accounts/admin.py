from django.contrib import admin
from .models import UserAccountProfile

admin.site.register(UserAccountProfile)
class UserAccountProfileInline(admin.StackedInline):
    model = UserAccountProfile
    can_delete = False

