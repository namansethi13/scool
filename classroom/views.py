from django.views.generic import CreateView, TemplateView
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.utils.encoding import force_str 
from django.urls import reverse_lazy
from django.contrib import messages
from .models import BaseUser
from .forms import SignUpForm
from .custom_decorators import logout_required
import logging
import random
logger = logging.getLogger(__name__)


# from .utils import check_email, send_activation_email, format_email_message  



class SignUpView(CreateView):
    """
    SignUp View for Corporate and College
    """
    @method_decorator(logout_required)
    def get(self, request):
        """
        renders corporate and college form
        """
        context = {
            'signup_form' : SignUpForm()
        }
        return render(request, 'signup.html', context)

    @method_decorator(logout_required)
    def post(self, request):
        """
        Check the role and accordingly validate the post data
        """
        try:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            pass1 =  request.POST['password1']
            pass2 =  request.POST['password2']
            if pass1 != pass2:
                messages.warning(request,"password do not match")
                logger.info("password do not match")
                return redirect(reverse_lazy('signup'))
            form = SignUpForm(request.POST)
            # check email entered is already is in database
            # redirect_url = check_email(request, request.POST.get('email',None))
            # if redirect_url != None:
            #     return redirect(redirect_url)
            if form.is_valid():
                print("Form is valid")
                email = form.cleaned_data.get('email')
                username = email.split('@')[0] + str(random.randint(0,99999))
                password= form.cleaned_data.get('password1')
                user = BaseUser.objects.create(username=username, email=email, 
                password=password, first_name=fname, last_name=lname)
                user.set_password(password)
                user.save()
                logger.info("Registration Successfull!!")

                # message = format_email_message(request, user)
                # send_activation_email.delay(message, email)
                # logger.info(f"email sent to {email}")
                # messages.success(request,f"check {email} to get a verification link")
            else:
                messages.warning(request,"Form data is invalid")
            return redirect(reverse_lazy('signup'))
        except:
            logger.error("Error: Some exception occurred at post request")
            messages.error(request, "Error: Some exception occurred at post request")
            return redirect(reverse_lazy('home'))



class HomePageView(TemplateView):
    """
    Home Page of Website
    """
    def get(self, request):
        if request.user.is_authenticated:
            username = request.user.username
        else:
            username = null
        context = {username}
        return render(request, 'home.html')
