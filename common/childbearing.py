# Childbearing class
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
    
    # output all parameters with description
    def describe(self):
        print(f'Age of childbearing: {self.age}')
        print(f'Expense of preparation: {self.preparation}')
        print(f'Expense of birth: {self.birth}')
        print(f'Expense of postpartum recovery: {self.postpartum_recovery}')
        print(f'Expense of kindergarden: {self.kindergarden}')
        print(f'Expense of primary school: {self.primary_school}')
        print(f'Expense of middle school: {self.middle_school}')
        print(f'Expense of high school: {self.high_school}')
        print(f'Expense of college: {self.college}')
    
