import collections
from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses(data/spending_data.csv)
spending_categories = []
for expense in expenses.list:
    expense.category.append(spending_categories)

spending_counter = collections.Counter(spending_categories)
print(spending_counter)

/Users/marksmyth/Downloads/pluralsight-projects-python-collections-budget-0552413/data/spending_data.csv