from django import forms

from .models import LeadRequest


class LeadRequestForm(forms.ModelForm):
    class Meta:
        model = LeadRequest
        fields = ["name", "phone", "message"]

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "")
        digits = "".join(char for char in phone if char.isdigit())
        if len(digits) < 10:
            raise forms.ValidationError("Введите номер телефона минимум из 10 цифр.")
        return phone
