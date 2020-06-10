from django import forms
from .models import Appointment, Expense
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class NewAppointmentUserForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Appointment
        exclude = ['name', 'email', 'status', 'cost', 'submitted_at', 'user', 'key']

class NewAppointmentStaffForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Appointment
        exclude = ['submitted_at', 'user', 'key']

class NewExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('expense', 'amount', 'purchaser', 'paid')
 
