class Retirement:
    def __init__(self, retirement):
        self.age = retirement
    
    
    def __str__(self):
        return 'Retirement: %s' % (self.age)
    
    # describe all attributes
    def describe(self):
        print('Retirement age: %s' % self.age)