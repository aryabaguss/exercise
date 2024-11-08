from tabulate import tabulate







class User:
    user= {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
    }
    
    plan = {
    "Services" : ['Stream', 'Download','SD Quality','HD Quality','UHD Quality','Number of Devices','Content Variety','Price'],
    "Basic Plan":['\u2713','\u2713','\u2713','\u00D7','\u00D7',1,'3rd party Movie Only', 120_000],
    "Standard Plan":['\u2713','\u2713','\u2713','\u2713','\u00D7',2,'Basic Plan + Sports (F1, Football, Basketball)',160_000],
    "Premium Plan":['\u2713','\u2713','\u2713','\u2713','\u2713',4,'Basic Plan + Standard Plan + Pacflix Original Series',200_000]
    }
    
    compare = {
    "Basic Plan": 1, "Standard Plan": 2, "Premium Plan": 3
    }

    list_plan = list(plan.keys())
    list_user = list(user.keys())


    def __init__(self,username,current_plan,duration_plan):
        self.username = username
        self.current_plan = current_plan.title()
        self.duration_plan = duration_plan

        if self.username not in (self.list_user):
          raise ValueError("Username didn't exist!")

        if self.current_plan not in (self.list_plan):
          raise ValueError("Plan didn't exist!")

    def check_benefit(self):
        print()
        print('Pacflix Plan List')
        print(tabulate(self.plan, headers = "keys" ,tablefmt='fancy_grid'))
        print()

    def check_plan(self):
        benefit = {
            "Services" : self.plan['Services'],
            "Plan" : self.plan[self.current_plan]
        }
        print(f'Username      : {self.username}')
        print(f'Current Plan  : {self.current_plan}')
        print(f'Duration Plan : {self.duration_plan} Months')
        print()
        print(f'{self.current_plan} Pacflix Benefit List')
        print(tabulate(benefit, headers = ['Services', self.current_plan] ,tablefmt='fancy_grid'))
        print()

    def upgrade_plan(self,new_plan):
        self.new_plan = new_plan.title()
        if self.new_plan not in (self.list_plan):
            raise Exception("Plan didn't exist!")
        else:
            pass

        plan_price = self.plan[self.new_plan][-1]
        if self.compare[self.current_plan] < self.compare[new_plan]:
            if self.duration_plan > 12:
                discount = (5/100)
            else:
                discount = 0

            final_price = plan_price - (plan_price * discount)
            print(f'Price for upgrading to {self.new_plan}: Rp {final_price:,}')

        elif self.compare[self.current_plan] == self.compare[new_plan]:
            print(f"{new_plan} is your current plan, please choose another plan.")

        else:
            print(f"Your current plan is {self.current_plan}. You can't Downgrade your plan.")

class New_User:
    def __init__(self,username):
        self.username = username

    def check_benefit(self):
        print()
        print('Pacflix Plan List')
        print(tabulate(User.plan, headers = "keys" ,tablefmt='fancy_grid'))
        print()

    def pick_plan(self,new_plan,referral_code):
        self.new_plan = new_plan.title()
        self.referral_code = referral_code
        if self.new_plan not in (User.list_plan):
            raise Exception("Plan didn't exist!")
        else:
            pass

        plan_price = User.plan[self.new_plan][-1]

        list_values = []
        for sublist in User.user.values():
            for item in sublist:
                list_values.append(item)

        if referral_code in (list_values):
            print('Referral Code is Available')
            discount = (4/100)
        else:
            raise Exception("Referral Code doesn't Exist")

        final_price = plan_price - (plan_price * discount)
        print(f'Total Price for {self.new_plan}: Rp {final_price:,}')



'''Case Study 1: User Check all plan benefit '''
print()    
print('==== STUDY CASE 1 ====')
user_1 = User('Shandy','basic plan',12)
print(user_1.username, user_1.current_plan, user_1.duration_plan)
user_1.check_benefit()


'''Case Study 2: user check current plan and show benefit'''
print('==== STUDY CASE 2 ====')
user_2 = User('Cahya','standard plan',24)
user_2.check_plan()


'''Case Study 3: user want to upgrade plan'''
print('==== STUDY CASE 3 ====')
user_3 = User('Cahya','Standard Plan',24)
user_3.check_benefit()
user_3.check_plan()
user_3.upgrade_plan('Premium Plan')

'''Case Study 4: new user wants to pick a new plan and shows total price'''
print()
print('==== STUDY CASE 4 ====')
faizal = New_User('Faizal_icikiwir')
faizal.check_benefit()
faizal.pick_plan('basic Plan','bagus-9f92')
