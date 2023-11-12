from django.contrib import admin
from .models import UserAccountProfile

admin.site.register(UserAccountProfile)
# class UserProfileInline(admin.StackedInline):
#     model = UserAccountProfile
#     can_delete = False
