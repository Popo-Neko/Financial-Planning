import pandas as pd

# life cycle of a person
class person:
    def __init__(self, name, age, life_events, income, expense):
        self.name = name
        self.age = age
        self.life_events = life_events
        self.incomes = income
        self.expenses = expense
        print(f'{self.name} is {self.age} now.')
        # calculate life time
        self.life_time = self.life_events.death.age - self.age + 1
        cash_flow = pd.DataFrame(columns=['age', 'marriage', 'purchase_house', 'childbearing', 'retirement', 'income', 
                                        'expense','year_balance'], 
                                        index=range(self.age, self.life_events.death.age+1))
        # create life time cash flow df
        cash_flow['age'] = cash_flow.index
        cash_flow['marriage'] = self.get_married()
        cash_flow['purchase_house'] = self.purchase_house()
        cash_flow['childbearing'] = self.childbearing()
        cash_flow['retirement'] = self.retirement()
        cash_flow['income'] = self.income()
        cash_flow['expense'] = self.expense()
        cash_flow['year_balance'] = cash_flow['marriage'] + cash_flow['purchase_house'] + cash_flow['childbearing'] + cash_flow['retirement'] + cash_flow['income'] + cash_flow['expense']
        self.cash_flow = cash_flow
        
    def get_married(self):
        data = [0 for i in range(self.life_time)]
        data[self.life_events.marriage.age - self.age] = -self.life_events.marriage.sum
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    
    def purchase_house(self):
        data = [0 for i in range(self.life_time)]
        data[self.life_events.purchase_house.age - self.age] = -self.life_events.purchase_house.down_payment
        for i in range(self.life_events.purchase_house.age -self.age, self.life_events.purchase_house.age -self.age + 31):
            data[i] = -self.life_events.purchase_house.monthly_mortgage
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    
    def childbearing(self):
        data = [0 for i in range(self.life_time)]
        data[self.life_events.childbearing.age - self.age] = -self.life_events.childbearing.preparation
        data[self.life_events.childbearing.age + 1 - self.age] = -self.life_events.childbearing.birth -self.life_events.childbearing.postpartum_recovery
        for i in range(self.life_events.childbearing.age + 3 -self.age, self.life_events.childbearing.age + 6 -self.age):
            data[i] = -self.life_events.childbearing.kindergarden
        for i in range(self.life_events.childbearing.age + 7 -self.age, self.life_events.childbearing.age + 13 -self.age):
            data[i] = -self.life_events.childbearing.primary_school
        for i in range(self.life_events.childbearing.age + 13 -self.age, self.life_events.childbearing.age + 16 -self.age):
            data[i] = -self.life_events.childbearing.middle_school
        for i in range(self.life_events.childbearing.age + 16 -self.age, self.life_events.childbearing.age + 19 -self.age):
            data[i] = -self.life_events.childbearing.high_school
        for i in range(self.life_events.childbearing.age + 19 -self.age, self.life_events.childbearing.age + 23 -self.age):
            data[i] = -self.life_events.childbearing.college
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    
    @staticmethod
    def MPF(monthly_salary, increase_rate, start_age, end_age, stop_age, MPF_return_rate):
        factor = 1 + MPF_return_rate/12
        MPF_total = 0
        for i in range(start_age, end_age+1):
            for j in range(1, 13):
                MPF_contributions = monthly_salary * 0.1
                MPF_total += MPF_contributions
                MPF_total = MPF_total * factor
            if i < stop_age:
                monthly_salary = monthly_salary * (1 + increase_rate)
        return MPF_total 
    
    def retirement(self):
        data = [0 for i in range(self.life_time)]
        mpf = self.MPF(self.incomes.salary, self.incomes.increase_rate, self.age, self.life_events.retirement.age, self.incomes.increase_stop_age, self.incomes.MPF_rate)
        for i in range(self.age, self.life_events.retirement.age):
            data[i] = mpf
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    
    def income(self):
        data = [0 for i in range(self.life_time)]
        for i in range(self.age, self.life_events.retirement.age+1):
            data[i] = self.incomes.salary
            if i < self.life_events.retirement.age:
                self.incomes.salary = self.incomes.salary * (1 + self.incomes.increase_rate)
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    
    def expense(self):
        data = [0 for i in range(self.life_time)]
        for i in range(self.age, self.life_events.retirement.age+1):
            if i < self.life_events.purchase_house.age:
                data[i] = self.expenses.monthly_expense + self.expenses.rent + self.expenses.contingency_expense
            else:
                data[i] = self.expenses.monthly_expense + self.expenses.contingency_expense
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))

# life events of a person
class life_events:
    def __init__(self, marriage, purchase_house, childbearing, retirement, death):
        self.marriage = marriage
        self.purchase_house = purchase_house
        self.childbearing = childbearing
        self.retirement = retirement
        self.death = death
        assert self.marriage.age >= 22, 'Marriage age should be greater than 22.'
        assert self.childbearing.age >= 22, 'Childbearing age should be greater than 22.'
        assert self.retirement.age >= 55, 'Retirement age should be greater than 55.'
        # retirement age should be greater than marriage age and childbearing age and greater than purchase_house age and less than death age
        assert self.retirement.age > self.marriage.age, 'Retirement age should be greater than marriage age.'
        assert self.retirement.age > self.childbearing.age, 'Retirement age should be greater than childbearing age.'
        assert self.retirement.age > self.purchase_house.age, 'Retirement age should be greater than purchase_house age.'
        assert self.retirement.age < self.death.age, 'Retirement age should be less than death age.'
        
    def __str__(self):
        return 'Marriage: %s, Purchase_house: %s, Childbearing: %s, Retirement: %s' % (self.marriage, self.purchase_house, self.childbearing, self.retirement)

    def __dict__(self):
        return {'Marriage': self.marriage, 'Purchase_house': self.purchase_house, 'Childbearing': self.childbearing, 'Retirement': self.retirement}
    
    def __getitem__(self, key):
        return getattr(self, key)


class Marriage:
    def __init__(self, marriage, location, tables, unit_price, ceremony, accommodation, wine, honeymoon, jewelry):
        # age of marriage
        self.age = marriage
        # location of wedding
        self.location = location
        # number of tables
        self.tables = tables
        # unit price of table
        self.unit_price = unit_price
        # ceremony
        self.ceremony = ceremony
        # accommodation
        self.accommodation = accommodation
        # wine
        self.wine = wine
        # honeymoon
        self.honeymoon = honeymoon
        # jewelry
        self.jewelry = jewelry
        self.sum = self.ceremony + self.accommodation + self.wine + self.honeymoon + self.jewelry + self.tables * self.unit_price

    def __str__(self):
        return 'Marriage: %s' % (self.age)

    def __dict__(self):
        return {'Marriage': self.age}

    def __getitem__(self, key):
        return getattr(self, key)


class Purchase_house:
    def __init__(self, purchase_house, location, area, price, down_payment_ratio, loan, mortgage_ir, renovation, furniture, appliances):
        # age of purchase house
        self.age = purchase_house
        # location of house
        self.location = location
        # area of house
        self.area = area
        # price of house
        self.price = price
        # unit price of house
        self.unit_price = price / area
        # down payment ratio
        self.down_payment = down_payment_ratio
        # down payment
        self.down_payment = price * down_payment_ratio
        # loan
        self.loan = price - self.down_payment
        # interest rate
        self.interest_rate = mortgage_ir
        # renovation
        self.renovation = renovation
        # furniture
        self.furniture = furniture
        # appliances
        self.appliances = appliances
        # monthly mortgage
        self.monthly_mortgage = self.loan * (self.interest_rate*(1+self.interest_rate)**(30*12)) / ((1+self.interest_rate)**(30*12)-1)  
        
    def __str__(self):
        return 'Purchase_house: %s' % (self.age)


class Childbearing:
    def __init__(self, childbearing, preparation, birth, postpartum_recovery, kindergarden, primary_school, middle_school, high_school, college):
        # age of childbearing
        self.age = childbearing
        # expense of preparation
        self.preparation = preparation
        # expense of  birth
        self.birth = birth
        # expense of  postpartum recovery
        self.postpartum_recovery = postpartum_recovery
        # expense of  kindergarden
        self.kindergarden = kindergarden
        # expense of  primary school
        self.primary_school = primary_school
        # expense of  middle school
        self.middle_school = middle_school
        # expense of  high school
        self.high_school = high_school
        # expense of  college
        self.college = college
    
    def __str__(self):
        return 'Childbearing: %s' % (self.age)


class Retirement:
    def __init__(self, retirement):
        self.age = retirement
    
    
    def __str__(self):
        return 'Retirement: %s' % (self.age)
    

class Death:
    def __init__(self, death):
        self.age = death
    
    def __str__(self):
        return 'Death: %s' % (self.age)


def tax(annual_income):
    # HK tax
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

    
if __name__ == '__main__':
    Marriage_1 = Marriage(25, 'Beijing', 20, 10000, 10000, 10000, 10000, 10000, 10000)
    Purchase_house_1 = Purchase_house(30, 'Beijing', 100, 1000000, 0.3, 700000, 0.05, 100000, 100000, 100000)
    Childbearing_1 = Childbearing(35, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000)
    Retirement_1 = Retirement(60)
    Death_1 = Death(85)
    life_events_1 = life_events(Marriage_1, Purchase_house_1, Childbearing_1, Retirement_1, Death_1)
    income_1 = income(20000, 0.05, 0.05, 35)
    expense_1 = expense(10000, 5000, 100000)
    person_1 = person('Jack', 20, life_events_1, income_1, expense_1)
    print(person_1.cash_flow)
    
