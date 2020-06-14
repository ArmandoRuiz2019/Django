from django import forms
from django.conf import settings
from core.mail import send_mail_template


class ContactoCurso(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Tu Nombre", 'required': "required"}))
    telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "Tu Numero Celular", 'required': "required"}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Tu Email", 'required': "required"}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Tu Comentario"}))

    def send_mail(self, nombre):
        subject = 'INTERESADO EN LOS CURSOS DE PYTHON'
        context = {
            'nombre': self.cleaned_data['nombre'],
            'email': self.cleaned_data['email'],
            'telefono': self.cleaned_data['telefono'],
            'mensaje': self.cleaned_data['mensaje'],
        }
        template_name = 'contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )
