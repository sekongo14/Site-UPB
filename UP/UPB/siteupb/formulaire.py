from django.forms import ModelForm
from .models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['Nom', 'Prenom', 'Contact', 'email', 'message']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Nom'].widget.attrs.update({
            'class' : 'form-input', 
            'id' : "contact-first-name",
            'name':"first-name", 
            'type':"text",   
        })

        self.fields['Prenom'].widget.attrs.update({
            'id' : "contact-last-name",
            'type': "text", 
            'name': "last-name",
            'class': "form-input",
        })


        self.fields['email'].widget.attrs.update({
            'class':"form-input",
            'id': "contact-email",
            'type': "email",
            'name': "email",
        })

        self.fields['Contact'].widget.attrs.update({
           'class': "form-input",
            'id': "contact-phone",
            'type': "text", 
            'name':"phone",
        })

        self.fields['message'].widget.attrs.update({
          'class': "form-input",
          'id': "contact-message",
          'name': "message",
        })




