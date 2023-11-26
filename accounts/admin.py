from django.contrib import admin

from .models import User, UserProfile, TransactionDiary, Transaction


admin.site.register(UserProfile)
admin.site.register(TransactionDiary)
admin.site.register(Transaction)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
