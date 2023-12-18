# Income class
def tax(annual_income, tax_policy = 'HK'):
    # HK tax
    if tax_policy == 'HK':
        if annual_income <= 50000:
            tax = annual_income * 0.02
        elif annual_income <= 100000:
            tax = 1000 + (annual_income - 50000) * 0.06
        elif annual_income <= 150000:
            tax = 4000 + (annual_income - 100000) * 0.1
        elif annual_income <= 200000:
            tax = 9000 + (annual_income - 150000) * 0.14
        else:
            tax = 16000 + (annual_income - 200000) * 0.17
        return tax


class income:
    def __init__(self, salary, increase_rate, MPF_rate, stop_age):
        # salary
        self.salary = salary
        # wage increase rate
        self.increase_rate = increase_rate
        # MPF interest rate
        self.MPF_rate = MPF_rate
        # tax 
        self.annual_tax = tax(salary * 12)
        # increase stop age
        self.increase_stop_age = stop_age
    
    def __str__(self):
        return 'Salary: %s' % (self.salary)