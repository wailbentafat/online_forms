import graphene
from graphene_django.types import DjangoObjectType
from .models import Form, Formfield, Response, ResponseField

class FormfieldType(DjangoObjectType):
    class Meta:
        model = Formfield

    response = graphene.Field(lambda: ResponseType)  
    def resolve_response(self, info):
        return self.response 

class FormType(DjangoObjectType):
    form_fields = graphene.List(FormfieldType) 

    class Meta:
        model = Form

    def resolve_form_fields(self, info):
        return self.formfields.all()  

class ResponseFieldType(DjangoObjectType):
    class Meta:
        model = ResponseField

    response = graphene.Field(lambda: ResponseType) 
    def resolve_response(self, info):
        return self.response  
class ResponseType(DjangoObjectType):
    response_field = graphene.Field(ResponseFieldType)  

    class Meta:
        model = Response

    def resolve_response_field(self, info):
        return self.response_field  
class query(graphene.ObjectType):
    form = graphene.Field(FormType, id=graphene.Int())
    response = graphene.Field(ResponseType, id=graphene.Int())

    def resolve_form(self, info, id):
        return Form.objects.get(id=id)
    def resolve_response(self, info, id):
        return Response.objects.get(id=id)