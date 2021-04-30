from django.contrib.auth.models import User
from .models import Category,Quizzes,Question,Answer
from django.contrib.auth.hashers import make_password
from graphene_django import DjangoObjectType
import graphene


#QuerySet
class UserType(DjangoObjectType):
    class Meta:
        model = User
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
#Mutation
class CreateUser(graphene.Mutation):
    class Input:
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()
    ok = graphene.Boolean()
    def mutate(self,info,**args):
        created_user = User.objects.create(username=args.get('username'))
        created_user.password = make_password(args.get('password'))
        created_user.save()
        # user_name=UserType(username=args.get('username'))
        ok=True
        return CreateUser(ok=ok)

class UpdateUser(graphene.Mutation):
    class Input:
        id = graphene.Int()
        user_name = graphene.String()
        password = graphene.String()
        email = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
    ok=graphene.Boolean()
    def mutate(self,info,**args):
        user_update = User.objects.get(id=args.get('id'))
        user_update.username = args.get('user_name',user_update.username)
        user_update.password = make_password(args.get('password',user_update.password))
        user_update.email = args.get('email',user_update.email)
        user_update.first_name = args.get('first_name',user_update.first_name)
        user_update.last_name = args.get('last_name',user_update.last_name)
        user_update.save()
        ok=True
        return UpdateUser(ok=ok)

class DeleteUser(graphene.Mutation):
    class Input:
        id=graphene.Int()

    ok = graphene.Boolean()
    def mutate(self,info,**args):
        delete_user = User.objects.get(id=args.get('id'))
        delete_user.delete()
        ok=True
        return DeleteUser(ok=ok)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    update_user = UpdateUser.Field()

class Query(graphene.ObjectType):
    all_quizzes = graphene.List(QuizzesType,id=graphene.Int())
    all_question = graphene.List(QuestionType,id=graphene.Int())
    all_category = graphene.List(CategoryType,id=graphene.Int())
    all_answer = graphene.List(AnswerType,id=graphene.Int())
    users = graphene.List(UserType, id=graphene.Int())

    def resolve_users(self, info, **args):
        if args.get('id'):
            return User.objects.filter(pk=args.get('id'))
        else:
            return User.objects.all()

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

schema = graphene.Schema(query=Query ,mutation=Mutation)
