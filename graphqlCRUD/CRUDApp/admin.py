from django.contrib import admin

# Register your models here.
from .models import Category,Question,Quizzes,Answer
admin.site.register(Category)
admin.site.register(Quizzes)
admin.site.register(Question)
admin.site.register(Answer)