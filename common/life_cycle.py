import pandas as pd
from common.childbearing import Childbearing
from common.death import Death
from common.marriage import Marriage
from common.purchase_house import Purchase_house
from common.retirement import Retirement
from common.income import income
from common.expense import expense
from common.life_events import life_events
from func import MPF
 

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
        
        # create life time cash flow df for plot and calculate
        cash_flow = pd.DataFrame(index=range(self.age, self.life_events.death.age+1))
        cash_flow['age'] = cash_flow.index
        cash_flow['marriage'] = self.get_married()
        cash_flow['purchase_house'] = self.purchase_house()
        cash_flow['childbearing'] = self.childbearing()
        cash_flow['retirement'] = self.retirement()
        cash_flow['monthly_income'] = self.income()
        cash_flow['monthly_expense'] = self.expense()
        cash_flow['year_balance'] = -cash_flow['marriage'] -cash_flow['purchase_house'] -cash_flow['childbearing'] +cash_flow['retirement'] + 12*cash_flow['monthly_income'] -12*cash_flow['monthly_expense']
        cash_flow['accumulated_balance'] = cash_flow['year_balance'].cumsum()
        self.cash_flow = cash_flow
        
        # create life time cash flow table for display
        cash_flow_table = cash_flow.copy()
        for i in cash_flow_table.columns:
            if i != 'age':
                cash_flow_table[i] = cash_flow_table[i].round(2).apply(lambda x: '{:,.2f}'.format(x))
        self.cash_flow_table = cash_flow_table
        
    def get_married(self):
        data = [0 for i in range(self.life_time)]
        data[self.life_events.marriage.age - self.age] = self.life_events.marriage.sum
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    
    def purchase_house(self):
        data = [0 for i in range(self.life_time)]
        data[self.life_events.purchase_house.age - self.age] = self.life_events.purchase_house.monthly_mortgage*12 + self.life_events.purchase_house.down_payment + self.life_events.purchase_house.renovation + self.life_events.purchase_house.furniture + self.life_events.purchase_house.appliances
        for i in range(self.life_events.purchase_house.age -self.age + 1, self.life_events.purchase_house.age -self.age + 31):
            data[i] = self.life_events.purchase_house.monthly_mortgage*12
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    
    def childbearing(self):
        data = [0 for i in range(self.life_time)]
        data[self.life_events.childbearing.age - self.age] = self.life_events.childbearing.preparation
        data[self.life_events.childbearing.age + 1 - self.age] = self.life_events.childbearing.birth +self.life_events.childbearing.postpartum_recovery
        for i in range(self.life_events.childbearing.age + 2 -self.age, self.life_events.childbearing.age + 6 -self.age):
            data[i] = self.life_events.childbearing.kindergarden
        for i in range(self.life_events.childbearing.age + 6 -self.age, self.life_events.childbearing.age + 12 -self.age):
            data[i] = self.life_events.childbearing.primary_school
        for i in range(self.life_events.childbearing.age + 12 -self.age, self.life_events.childbearing.age + 15 -self.age):
            data[i] = self.life_events.childbearing.middle_school
        for i in range(self.life_events.childbearing.age + 15 -self.age, self.life_events.childbearing.age + 18 -self.age):
            data[i] = self.life_events.childbearing.high_school
        for i in range(self.life_events.childbearing.age + 18 -self.age, self.life_events.childbearing.age + 22 -self.age):
            data[i] = self.life_events.childbearing.college
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    
    def retirement(self):
        data = [0 for i in range(self.life_time)]
        mpf = MPF(self.incomes.salary, self.incomes.increase_rate, self.age, self.life_events.retirement.age, self.incomes.increase_stop_age, self.incomes.MPF_rate)
        data[self.life_events.retirement.age - self.age] = mpf
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    
    def income(self):
        data = [0 for i in range(self.life_time)]
        for i in range(0, self.life_events.retirement.age-self.age+1):
            data[i] = self.incomes.salary
            if i < self.incomes.increase_stop_age - self.age:
                self.incomes.salary = self.incomes.salary * (1 + self.incomes.increase_rate)
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    
    def expense(self):
        data = [0 for i in range(self.life_time)]
        for i in range(0, self.life_events.death.age-self.age+1):
            if i + self.age < self.life_events.purchase_house.age:
                data[i] = self.expenses.monthly_expense + self.expenses.rent + self.expenses.contingency_expense
            else:
                data[i] = self.expenses.monthly_expense + self.expenses.contingency_expense
        return pd.Series(data, index=range(self.age, self.life_events.death.age+1))
    

    
if __name__ == '__main__':
    Marriage_1 = Marriage(25, 'Beijing', 20, 10000, 10000, 10000, 10000, 10000, 10000)
    Purchase_house_1 = Purchase_house(30, 'Beijing', 100, 6210000, 0.2, 0.049, 100000, 100000, 100000)
    Childbearing_1 = Childbearing(35, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000)
    Retirement_1 = Retirement(60)
    Death_1 = Death(85)
    life_events_1 = life_events(Marriage_1, Purchase_house_1, Childbearing_1, Retirement_1, Death_1)
    income_1 = income(20000, 0.05, 0.05, 35)
    expense_1 = expense(10000, 5000, 100000)
    person_1 = person('Jack', 20, life_events_1, income_1, expense_1)
    print(person_1.cash_flow.head(60))
