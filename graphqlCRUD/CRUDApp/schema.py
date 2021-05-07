# from django.contrib.auth.models import User
from .models import Category,Quizzes,Question,Answer,ExtendUser
from django.contrib.auth.hashers import make_password
from graphene_django import DjangoObjectType
from graphql_auth import mutations
import graphene



#QuerySet
class UserType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields=('id','username','password','email')

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")
class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")

class Query(graphene.ObjectType):
    all_quizzes = graphene.List(QuizzesType,id=graphene.Int())
    all_question = graphene.List(QuestionType,id=graphene.Int())
    all_category = graphene.List(CategoryType,id=graphene.Int())
    all_answer = graphene.List(AnswerType,id=graphene.Int())
    users = graphene.List(UserType, id=graphene.Int())

    def resolve_users(self, info, **args):
        if args.get('id'):
            return ExtendUser.objects.filter(pk=args.get('id'))
        else:
            return ExtendUser.objects.all()

    def resolve_all_quizzes(self,info,**args):
        if args.get('id'):
            return Quizzes.objects.filter(id=args.get('id'))
        else:
            return Quizzes.objects.all()

    def resolve_all_question(self,info,**args):
        if args.get('title'):
            return Question.objects.get(title=args.get('title'))
        else:
            return Question.objects.all()

    def resolve_all_category(self,info,**args):
        if args.get('id'):
            return Category.objects.get(pk=args.get('id'))
        else:
            return Category.objects.all()

    def resolve_all_answer(self,info,**args):
        if args.get('question'):
            return Answer.objects.get(question=args.get('question'))
        else:
            return Answer.objects.all()

# Mutation
class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()

class Mutation(AuthMutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query ,mutation=Mutation)
