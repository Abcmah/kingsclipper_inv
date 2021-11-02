from django import forms
from django.forms import ModelForm 
from .models import *

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['service','service_by','amount','payment_mode','status','client_balance']
        widgets={
            'service':forms.Select(attrs={"class":"form-control"}),
            'service_by':forms.Select(attrs={'class':'form-control'}),
            'amount':forms.TextInput(attrs={'class':'form-control'}),
            'payment_mode':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'client_balance':forms.TextInput(attrs={'class':'form-control'})
        }

class EmpExpenseForm(ModelForm):
    class Meta:
        model = EmpExpense
        fields = ['name','amount','paid','date_repay']
        widgets = {
            'name':forms.Select(attrs={'class':'form-control'}),
            'amount':forms.TextInput(attrs={'class':'form-control'}),
            'paid':forms.TextInput(attrs={'class':'form-control'}),
            'date_repay':forms.DateInput(attrs={'class':'form-control'})
        }
       
class ExpenseForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['item','quantity','descriptions','cost','supplier']
        widgets={
            'item':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.TextInput(attrs={'class':'form-control'}),
            'descriptions':forms.TextInput(attrs={'class':'form-control'}),
            'cost':forms.TextInput(attrs={'class':'form-control'}),
            'supplier':forms.TextInput(attrs={'class':'form-control'})
        }