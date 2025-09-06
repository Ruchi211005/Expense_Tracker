from django import forms
from .models import Expense,Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date', 'description']

def save(self,commit=True):
    instance=super().save(commit=False)
    if instance.category_obj:
        instance.category=instance.category_obj.name
    if commit:
        instance.save()
    return instance