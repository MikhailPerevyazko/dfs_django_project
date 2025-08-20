from django import forms
from .models import TrainingRegistration


class TrainingRegistrationForm(forms.ModelForm):
    class Meta:
        model = TrainingRegistration
        fields = ['child_name', 'birth_date', 'phone_number', 'planned_date', 'agreement']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'planned_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'child_name': forms.TextInput(attrs={'placeholder': 'Например, Иванов Иван Иванович'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+7 (999) 123-45-67'}),
        }
        labels = {
            'child_name': 'Введите имя ребенка:',
            'birth_date': 'Дата рождения:',
            'phone_number': 'Номер телефона:',
            'planned_date': 'Когда планируете подойти?',
            'agreement': 'Я даю согласие на обработку персональных данных',
        }