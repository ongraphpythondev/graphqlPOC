from django.contrib import admin
from django.apps import apps
# Register your models here.
from .models import Category,Question,Quizzes,Answer,ExtendUser
admin.site.register(ExtendUser)
admin.site.register(Category)
admin.site.register(Quizzes)
admin.site.register(Question)
admin.site.register(Answer)

app = apps.get_app_config('graphql_auth')
for model_name ,model in app.models.items():
    admin.site.register(model)