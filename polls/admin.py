from django.contrib import admin
from polls import models


# Register your models here.


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date','question_text']

# class Choicestack(admin.StackedInline):
#     model=models.choice
#     extra = 3

class ChoiceInline(admin.TabularInline):
    """"""
    model = models.choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    list_display = ('question_text', 'pub_date')

    inlines = [ChoiceInline]

    list_filter = ['pub_date']

    search_fields = ['question_text']


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.choice)
