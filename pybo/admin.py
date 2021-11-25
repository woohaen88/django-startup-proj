from django.contrib import admin
from .models import Question


# 제목으로 질문을 검색할 수 있도록 검색 항목을 추가
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# Register your models here.
admin.site.register(Question, QuestionAdmin)

