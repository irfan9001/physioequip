from django import forms
from .models import ContactQuery

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactQuery
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-3', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg rounded-3', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-3', 'placeholder': 'Phone Number (Optional)'}),
            'subject': forms.TextInput(attrs={'class': 'form-control form-control-lg rounded-3', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control form-control-lg rounded-3', 'placeholder': 'Your Message', 'rows': 5}),
        }
