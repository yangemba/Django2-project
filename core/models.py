from django.db import models
from problem_post.models import ProblemTopic
# Create your models here.
from django.contrib.auth.models import User
from message.models import Message


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, blank=True)
    messages = models.ManyToManyField(Message, null=True, blank=True)
    photo = models.ImageField(blank=True)
    date_reg = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True


class MasterProfile(Profile):
    speciality = models.CharField(max_length=50)
    about = models.TextField()
    total_money_earn = models.IntegerField(default=0, blank=True)
    problems_solved = models.ForeignKey(ProblemTopic, blank=True, null=True, on_delete=models.CASCADE)


class ClientProfile(Profile):
    total_money_spend = models.IntegerField(default=0, blank=True)
    problems_was = models.ForeignKey(ProblemTopic, null=True, blank=True, on_delete=models.CASCADE)











