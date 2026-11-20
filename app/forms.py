from django import forms

from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['inquiry_type', 'name', 'email', 'phone', 'message']
        widgets = {
            'inquiry_type': forms.Select(attrs={
                'class': 'w-full border border-gray-300 px-4 py-4 bg-white outline-none focus:border-resort-red focus:ring-1 focus:ring-resort-red',
                'required': True,
            }),
            'name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'email'}),
            'phone': forms.TelInput(attrs={'class': 'form-control', 'autocomplete': 'tel'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }
