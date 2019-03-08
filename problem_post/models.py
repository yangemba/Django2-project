from django.db import models
from django.contrib.auth.models import User


class ProblemTopic(models.Model):
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    problem_photo = models.ImageField(blank=True)
    money_offer = models.IntegerField()
    in_progress = models.BooleanField(default=False, blank=True)
    done = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    performer = models.ForeignKey(User, related_name='performer', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
