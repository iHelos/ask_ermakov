from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# __DJANGO-user__
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
def index(request):
    sort = request.GET.get('sort')
    if sort == 'hot':
        question_list = Question.objects.order_by('-rating').all()
    else:
        question_list = Question.objects.order_by('-date_added').all()

    pagedQuestion = Paginator(question_list, 20)
    page = request.GET.get('page')
    try:
		question_page = pagedQuestion.page(page)
    except PageNotAnInteger:
		question_page = pagedQuestion.page(1)
    return render(request, 'index.html',
                  {'question_page': question_page, 'last_page_number': pagedQuestion.num_pages, 'sort': sort})


def register(request):
    next = '/settings'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = RegistrationProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user_obj = form.save()
            profile_obj = profile_form.save(user=user_obj)
            user_obj = authenticate(username=user_obj.username, password=request.POST['password1'])
            login(request, user_obj)
            return HttpResponseRedirect(next)
    else:
        form = RegistrationForm()
        profile_form = RegistrationProfileForm()
    return render(request, 'user/signup.html', {'form': form, 'profile_form': profile_form})


@login_required(login_url='/login')
def profile(request):
    user_obj = User.objects.get(id=request.user.id)
    profile_obj = Profile.objects.get(user=user_obj)
    if request.method == 'POST':
        profile_form = SettingsProfileForm(request.POST, request.FILES, instance=profile_obj)
        user_form = SettingsUserForm(request.POST, instance=user_obj)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(request.get_full_path())
    profile_form = SettingsProfileForm(instance=profile_obj)
    user_form = SettingsUserForm(instance=user_obj)
    return render(request, 'profile.html', {'profile_form': profile_form, 'user_form': user_form})


def ask(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, user=request.user)
        if form.is_valid():
            question = form.save()
            question.save()
            next = '/question?id=' + str(question.id)
            return HttpResponseRedirect(next)
    else:
        form = QuestionForm()
    return render(request, 'ask.html', {'form': form})


def question(request):
    id = request.GET.get('id')
    cur_question = Question.objects.get(id=id)
    answer_list = Answer.objects.filter(question_id=id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, user=request.user, question=cur_question)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(request.get_full_path())
    else:
        form = AnswerForm()
    return render(request, 'question.html', {'Question': cur_question, 'Answers': answer_list, 'form': form})
