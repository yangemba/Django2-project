from django.contrib import admin
from .models import MasterProfile, ClientProfile
from problem_post.models import ProblemTopic
from message.models import Message


admin.site.register(MasterProfile)
admin.site.register(ClientProfile)
admin.site.register(ProblemTopic)
admin.site.register(Message)



# Register your models here.
