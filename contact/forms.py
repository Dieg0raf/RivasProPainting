from django import forms
from .models import Projects

class QuoteForm(forms.ModelForm):
    JOB_CHOICES = [
        ('', 'What type of painting'),
        ('Interior', 'Interior'),
        ('Exterior', 'Exterior'),
    ]

    job = forms.ChoiceField(choices=JOB_CHOICES, label='What type of painting')

    class Meta:
        model = Projects
        fields = ['first_name', 'last_name', 'user_email', 'user_phone', 'job' ,'job_desc']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control line-for-form', 'placeholder': 'Ex: Alex'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control line-for-form', 'placeholder': 'Ex: Tuner'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control line-for-form', 'placeholder': 'Ex: example@email.com'}),
            'user_phone': forms.TextInput(attrs={'class': 'form-control line-for-form', 'placeholder': 'Ex: 123-456-7891'}),
            'job_desc': forms.Textarea(attrs={'class': 'form-control area-for-form', 'placeholder': 'Ex: I need some cabinets painted.'}),
            'job': forms.Select(attrs={'class': 'form-control'})
        }

