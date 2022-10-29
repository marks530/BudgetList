#import budget
from . import Expense


class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def Append():
        def __init__(self, item):
            if self.sum_expenses + item < self.budget:
                self.expenses.append(item)
                self.sum_expenses += item
            else:
                self.overages.append(item)
                self.sum_overages += item

    def __len__(self):
        return len(sum(self.expenses)), len(self.overages)


def main():
    myBudgetList = BudgetList(budget:1200)


if __name__ == "__main__":
    main()

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

for expense in expenses.list:
    myBudgetList.append(expense.amount)
    print(str(len(myBudgetList)))

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()

