from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    # CATEGORY_CHOICES = [
    #     ("food", "Food"),
    #     ("travel", "Travel"),
    #     ("shopping", "Shopping"),
    #     ("other", "Other"),
    # ]
    title = models.CharField(max_length=100)   # short name for expense
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., 199.99
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  #choices=CATEGORY_CHOICES)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)  # optional notes

    def __str__(self):
        return f"{self.title} - {self.amount}"
# Create your models here.
