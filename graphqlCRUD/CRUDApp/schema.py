from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from graphene_django import DjangoObjectType
import graphene


#QuerySet
class UserType(DjangoObjectType):
    class Meta:
        model = User
        # fields=('id','username','password','email')
class Query(graphene.ObjectType):
    #Pass id field as query parameter
    users = graphene.List(UserType,id=graphene.Int())
    # @graphene.resolve_only_args
    def resolve_users(self,info,**args):
        if args.get('id') :
            return User.objects.filter(pk=args.get('id'))
        else:
            return User.objects.all()
#Mutation

class CreateUser(graphene.Mutation):
    class Input:
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()
    ok = graphene.Boolean()
    # us = graphene.Field(lambda : UserType)

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

schema = graphene.Schema(query=Query ,mutation=Mutation)
