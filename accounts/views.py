from urllib import response
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserCreationForm, OTPverificationForm
from .models import token

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("profile")
    template_name = "registration/signup.html"

    def create(self, request, *args, **kwargs):
        response = super(SignUpView, self).create(request, *args, **kwargs)
        
        return HttpResponse(response, status=201)

def profile(request):
    user = request.user
    
    if user.is_authenticated and not user.is_superuser:
        if request.method == 'GET':
            if  token.objects.get(user=user).is_used:
                return render(request, 'profile.html', {'user': user.email})
            else:
                form = OTPverificationForm()
                return render(request, 'registration\OTP-verification.html', {'form': form})

    if request.method == 'POST':
        
        if HttpResponse(token.objects.get(user=user).token==request.POST['code']):
            otpToken = token.objects.get(user=user)
            otpToken.is_used = True
            otpToken.save()
            return HttpResponseRedirect(request.path_info)
    
    return HttpResponseRedirect(reverse_lazy('login'))
    



        

