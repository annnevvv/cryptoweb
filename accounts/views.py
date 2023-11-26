from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile, TransactionDiary, Transaction

# Create your views here.


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class DashboardView(View):
    template_name = 'accounts/dashboard.html'

    def get(self, request, *args, **kwargs):

        user_profile = UserProfile.objects.get(user=request.user)
        user_transaction_diary = TransactionDiary.objects.get(
            user_profile=user_profile)
        user_transactions = Transaction.objects.filter(
            diary=user_transaction_diary).order_by('date_of_transaction')

        context = {'user_profile': user_profile,
                   'user_transaction_diary': user_transaction_diary,
                   'user_transactions': user_transactions}

        return render(request, self.template_name, context)
