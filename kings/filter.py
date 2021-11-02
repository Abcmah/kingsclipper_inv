import django_filters
from django import forms
from .models import *
from django_filters import DateFilter

class IncomeFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name ='time_posted',lookup_expr="gte")
    end_date = DateFilter(field_name="time_posted",lookup_expr='lte')
    class Meta:
        model = Income
        fields = ['service_by']

class ExpenseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date',lookup_expr='gte')
    end_date =DateFilter(field_name='date',lookup_expr='lte')
    class Meta:
        model=Expenses
        fields=['item']

class IndividualFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='time_posted',lookup_expr='gte')
    end_date =DateFilter(field_name='time_posted',lookup_expr='lte')
    class Meta:
        medel =Income
        fields=['service']
