from django.db import models
from django.contrib import admin


# Create your models here.

class Message(models.Model):
    Nom = models.CharField(max_length= 60, null= True, blank= True)
    Prenom = models.CharField(max_length= 70, null= True, blank= True)
    Contact = models.CharField(max_length= 20, null= False)
    email = models.EmailField(null= False)
    message = models.TextField(max_length= 300, null= False, blank= False)



class MessageAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'Prenom', 'Contact', 'email', 'message')