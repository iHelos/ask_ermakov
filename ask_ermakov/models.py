from django.db import models
from django.contrib.auth.models import User
from ask_ermakov import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    rating = models.IntegerField(default=0)
    avatar_url = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to=settings.uploads, default='default.jpg')


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Question(models.Model):
    author = models.ForeignKey(Profile)
    title = models.CharField(max_length=60)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    date_added = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    author = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    is_right = models.BooleanField(default=False)


class QuestionVote(models.Model):
    vote = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)


class AnswerVote(models.Model):
    vote = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    answer = models.ForeignKey(Answer)
