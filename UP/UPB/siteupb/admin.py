from django.contrib import admin
from .models import Message, MessageAdmin

# Register your models here.

admin.site.register(Message, MessageAdmin)
