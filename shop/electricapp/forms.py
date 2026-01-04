from django import forms
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=100,
        label="Повне ім'я",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Повне ім'я"
        })
    )

    phone = forms.CharField(
        max_length=20,
        label="Телефон",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Телефон"
        })
    )

    class Meta:
        model = ShippingAddress
        fields = ['city', 'address', 'postal_code']

        widgets = {
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Місто'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адреса доставки'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Поштовий індекс'
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.replace('+', '').isdigit():
            raise forms.ValidationError("Телефон повинен містити лише цифри")
        return phone
