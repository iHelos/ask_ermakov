from django.db import models
from django.contrib.auth.models import User
from ask_ermakov import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    rating = models.IntegerField(default=0)
    #avatar_url = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to=settings.uploads, default='default.jpg')

    def __unicode__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

class Question(models.Model):
    author = models.ForeignKey(Profile)
    title = models.CharField(max_length=60)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    is_right = models.BooleanField(default=False)

    def __unicode__(self):
        return self.text


class QuestionVote(models.Model):
    vote = models.IntegerField(default=0)
    user = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.vote


class AnswerVote(models.Model):
    vote = models.IntegerField(default=0)
    user = models.ForeignKey(Profile)
    answer = models.ForeignKey(Answer)

    def __unicode__(self):
        return self.vote
