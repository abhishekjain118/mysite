from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Title of Question', {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
                 ]
    inlines = [ChoiceInLine]
    #fields = ['pub_date', 'question_text'] #another way of presenting data

admin.site.register(Question, QuestionAdmin)
