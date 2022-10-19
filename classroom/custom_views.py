from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .custom_decorators import logout_required
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)

class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "You were successfully logged in."
    redirect_authenticated_user = True
    redirect_field_name = reverse_lazy('home')