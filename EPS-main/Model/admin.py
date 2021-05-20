from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Result)
admin.site.register(Quiz_2)


class AnswerInline (admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question , QuestionAdmin)
admin.site.register(Answer)