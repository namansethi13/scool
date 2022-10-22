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
import uuid
from django.conf import settings
from django.core.mail import send_mail
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
                auth_token=str(uuid.uuid4())#generates a token for specific user
                print(auth_token)#debug

                user = BaseUser.objects.create(username=username, email=email, 
                password=password, first_name=fname, last_name=lname,auth_token=auth_token)
                user.set_password(password)
                user.save()
                print("user created")

                
                #logger.info("Registration Successfull!!")
                send_mail_reg(email,auth_token)
                print("mail sent")
                return redirect('token')

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
            return redirect(reverse_lazy('login'))



class HomePageView(TemplateView):
    """
    Home Page of Website
    """
    def get(self, request):
        if request.user.is_authenticated:
            username = request.user.username
        else:
            username =' '
        context = {username}
        return render(request, 'home.html')



def token_send(request):
    return render(request,'token_send.html')



def verify(request,auth_token):
    try:
        user=BaseUser.objects.filter(auth_token=auth_token.first())
        if user.is_verified:
            if user:
                user.is_verified=True
                user.is_active=True
                user.save()
                messages.success(request,'your email have ben verififed .you can now login ')
                return redirect('login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)

def send_mail_reg(email,token):
    subject="your account need to be verified"
    message=f'hi paste the link to verify the account http://127.0.0.1:8000/verify/{token}'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)



def error(request):
    return render(request,'error.html')




