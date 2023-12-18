# Expense class
class expense:
    def __init__(self, monthly_expense, rent, contingency_expense):
        # monthly normal expense
        self.monthly_expense = monthly_expense
        # monthly rent
        self.rent = rent
        # contingency savings
        self.contingency_expense = contingency_expense
    
    def __str__(self):
        return 'Monthly_expense: %s' % (self.monthly_expense)