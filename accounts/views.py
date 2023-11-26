from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View

from .models import UserProfile, TransactionDiary

# Create your views here.


class DashboardView(View):
    template_name = 'accounts/dashboard.html'

    def get(self, request, *args, **kwargs):

        user_profile = UserProfile.objects.get(user=request.user)
        user_transaction_diary = TransactionDiary.objects.get(
            user_profile=user_profile)

        context = {'user_profile': user_profile,
                   'user_transaction_diary': user_transaction_diary}

        return render(request, self.template_name, context)
