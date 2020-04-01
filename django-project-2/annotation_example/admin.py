from django.contrib import admin
from annotation_example.models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
	pass

class ChoiceAdmin(admin.ModelAdmin):
	pass

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
