from django.urls import path
from . import views


urlpatterns = [
    path('', views.expense_list, name='expense_list'),  # homepage showing expenses
    path('add/', views.add_expense, name='add_expense'),  # page to add a new expense
    path('analyze/', views.analyze_expenses, name='analyze'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
     path('delete/<int:pk>/', views.delete_expense, name='delete_expense'), 
      path('edit/<int:pk>/', views.edit_expense, name='edit_expense'), 
]


