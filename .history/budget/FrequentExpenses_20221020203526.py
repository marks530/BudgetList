from signal import sigpending
from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses(data/spending_data.csv)
spending_categories = []
for expense in expenses.list:
    expense.category.append(spending_categories)
    
spending_    