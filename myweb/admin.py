from django.contrib import admin

from .models import Question, Choice, Order , ContactMail

admin.site.register(Question)
admin.site.register(ContactMail)
admin.site.register(Choice)
admin.site.register(Order)
