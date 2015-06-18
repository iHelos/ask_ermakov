from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#__DJANGO-user__
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from ask_ermakov.models import *
from ask_ermakov.forms import *
#    def hello(request):
#        output = 'Hello World <br/>'
#        if request.method == 'GET':
#            output += 'GET: <br/>'
#            string = request.GET.urlencode()
#            parameters = string.split("&")
#            for param in parameters:
#                output += param + '<br/>'
#        else:
#            output += 'POST: <br/>'
#            string = request.POST.urlencode()
#            string = split('&')
#            parameters = string.split("&")
#            for param in parameters:
#                output += param + '<br/>'
#        return HttpResponse(output)
def index (request):
    return  render(request, 'index.html', ())

def ask (request):
    return  render(request, 'ask.html', ())

def register(request):
	next = '/'
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		profile_form = RegistrationProfileForm(request.POST, request.FILES)
		if form.is_valid() and profile_form.is_valid():
			user_obj=form.save()
			profile_obj=profile_form.save(user = user_obj)
			user_obj=authenticate(username=user_obj.username, password=request.POST['password1'])
			login(request, user_obj)
			return HttpResponseRedirect(next)
	else:
		form = RegistrationForm()
		profile_form = RegistrationProfileForm()
	return render(request, 'user/signup.html', {'form': form, 'profile_form': profile_form})