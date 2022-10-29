#import budget
import


class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
    
    def Append():
        def __init__(self,item):
            if self.sum_expenses + item < self.budget:
                self.sum_expenses.append(item)
                self.sum_expenses += item
            else:
                self.overages.append(item)
                self.overages += item        
        
    def __len__(self):
        return len(sum(self.expenses)), len(self.overages)

    def main():
        myBudgetList = Budget