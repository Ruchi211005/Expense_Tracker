from pyexpat.errors import messages
from django.shortcuts import render, redirect,get_object_or_404
from .models import Expense,Category
from .forms import ExpenseForm,CategoryForm  # we will create this form next
from django.db.models import Sum
from datetime import date
from django.db.models.functions import TruncMonth, Coalesce

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":   # confirm before deleting
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/delete_confirm.html', {'expense': expense})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm

def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/edit_expense.html', {'form': form})

def analyze_expenses(request):
    # Totals by category (category is FK -> Category)
    categories = (
        Expense.objects
        .values('category__name')          # group by category name
        .annotate(total=Sum('amount'))    # sum amount per category
        .order_by('-total')
    )

    # Monthly totals (group by month)
    monthly = (
        Expense.objects
        .annotate(month=TruncMonth('date'))   # truncate date to month
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    # Convert QuerySets to lists so template can loop easily
    categories = list(categories)   # each item: {'category__name': 'Food', 'total': 1200.00}
    monthly = list(monthly)         # each item: {'month': datetime.date(2025, 9, 1), 'total': 230.00}

    return render(request, 'expenses/analyze.html', {
        'categories': categories,
        'monthly': monthly,
    })

def category_list(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'expenses/category_list.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_expense')
    else:
        form = CategoryForm()
    return render(request, 'expenses/add_category.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404


