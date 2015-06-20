from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from django import forms
from ask_ermakov.models import *


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ("username", "email")

    def save(self, commit=True):
        obj = super(RegistrationForm, self).save(commit=False)
        obj.username = self.cleaned_data["username"]
        obj.email = self.cleaned_data["email"]
        if commit:
            obj.save()
        return obj


class RegistrationProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationProfileForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].required = False

    class Meta:
        model = Profile
        fields = ("avatar",)

    def save(self, user, commit=True):
        obj = super(RegistrationProfileForm, self).save(commit=False)
        obj.user = user
        if commit:
            obj.save()
        return obj


class SettingsUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SettingsUserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def save(self, commit=True):
        obj = super(SettingsUserForm, self).save(commit=False)
        obj.username = self.cleaned_data['username']
        obj.email = self.cleaned_data['email']
        if commit:
            obj.save()
        return obj


class SettingsProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SettingsProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('avatar',)

    def save(self, commit=True):
        obj = super(SettingsProfileForm, self).save(commit=False)
        if commit:
            obj.save()
        return obj


class QuestionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['text'].required = True

    class Meta:
        model = Question
        exclude = ('author', 'rating', 'tags')

    def save(self, commit=True):
        obj = super(QuestionForm, self).save(commit=False)
        obj.author = self.user.profile
        if commit:
            obj.save()
        return obj


class AnswerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.question = kwargs.pop('question', None)
        super(AnswerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Answer
        fields = ('text',)

    def save(self, commit=True):
        obj = super(AnswerForm, self).save(commit=False)
        obj.question = self.question
        obj.author = self.user.profile
        if commit:
            obj.save()
        return obj
