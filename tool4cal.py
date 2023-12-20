'''
funcs for calculating
'''

def mortgage(loan, ir, n):
    '''
    cal a monthly payment mortgage with an identical amout for each month
    loan: loan amount = house price * (1 - down payment ratio)
    ir: annual interest rate for mortgage
    n: number of years for mortgage
    '''
    ir = ir / 12
    return loan * (ir*(1+ir)**(n*12)) / ((1+ir)**(n*12)-1)


# cal the present value of an annuity
def annuity(pmt, ir, n):
    '''
    cal the present value of an annuity
    pmt: payment for each period
    ir: annual interest rate
    n: number of periods
    '''
    ir = ir / 12
    return pmt * ((1 - (1+ir)**(-n*12)) / ir)
    

def MPF(monthly_salary, increase_rate, start_age, end_age, stop_age, MPF_return_rate):
    '''
    monthly_salary: monthly salary
    increase_rate: annual increase rate of salary
    start_age: start age of MPF
    end_age: end age of MPF
    stop_age: stop age of salary increase
    MPF_return_rate: annual return rate of MPF
    '''
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