from django.db import models
from django.contrib.auth.models import User

class Form(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    Created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user
class Formfield(models.Model):
    Forms_Field_type=(
        ('text','text'),
        ('number','number'),
        ('email','email'),
        ('url','url'),
        ('date','date'),
        ('time','time'),
        ('checkbox','checkbox'),
        ('file','file'),
    )
    form=models.ForeignKey(Form, on_delete=models.CASCADE)
    field_type=models.CharField(max_length=100, choices=Forms_Field_type)
    label=models.CharField(max_length=100)
    required=models.BooleanField(default=False)
    def __str__(self):
        return self.label
class Response(models.Model):
        submitted_at=models.DateTimeField(auto_now_add=True)
        user=models.ForeignKey(User, on_delete=models.CASCADE)
        form_field=models.OneToOneField(Formfield, on_delete=models.CASCADE)
        def __str__(self):
            return self.response
class ResponseField(models.Model):
        response = models.OneToOneField(Response, on_delete=models.CASCADE, related_name='response_fields')
        value = models.JSONField(default=dict)    
    
        
