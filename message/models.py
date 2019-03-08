from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    msg_content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)





