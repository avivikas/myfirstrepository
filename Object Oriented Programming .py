#!/usr/bin/env python
# coding: utf-8

# ###  Object Oriened Programming
# Objects are entities that represent instances of a general abstract concept called class. In Python, "attributes" are the variable defining an object state and the possble action are called "methods" 
# 
# ### 1- class
# class namesshould always be uppercase(it is naming convention)
# 
# syn- 
#    class ClassName(base_classes):
#         
#         statements      
# 
# #### __init__(self,)
# 
# __init__(self,...) will register/initialize your detail with google.
# 
# self will help you to get your respective details back when you click different tabs.

# In[31]:


class Account:
    def __init__(self, first_name = input('Enetr your first name  '),
                       last_name  = input('Enter your last name  '),
                       age        = int(input('Enter your age  ')),
                       user_id    = input('Enter your user_id  '),
                       passward   = input('Enter your passward  ')): #attributes/arguments
        
        #initialization
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
        self.user_id    = user_id
        self.passward   = passward
    
    def login(self):
        while True:
            signin = input('Enter your user_id  ')
            passward = input('Enter your passward  ')
            if signin == self.user_id and passward == self.passward:
                print('Successfully login')
                break
            else:
                print('User_id or passward is invalid')
                continue


# In[32]:


# instantiating a class and create an object for the class. Here bank is an object for class Account
bank = Account()


# In[33]:


# calling methods
bank.login()


# ### 2- Inheritance
# 
# In inheritance we need to copy properties of old class and add new properties or attributes and create new virsion of class that means we can say a new class inherit the properties or attributes of the old class. 

# In[34]:


class User_Account(Account):
    
    def __init__(self, acc_number, balance, *args):
        super(User_Account, self).__init__(*args)
        self.acc_number = acc_number
        self.balance = balance
    
    def user_details(self):
        while True:
            account = int(input('Enter the account numer'))
            if account == self.acc_number:
                print('Name = ', self.first_name)
                print('Age = ', self.age)
                print('Account Number = ', self.acc_number)
                print('Your balance = ', self.balance)
                break
            else:
                print('You entered wrong account number')
    
    def deposite(self):
        print('Your previous Balance is = ', self.balance)
        add_cash = int(input('Deposite Cash = '))
        self.balance += add_cash
        print('SBI Bank Rs. ',add_cash, 'deposite to your Account No ', self.acc_number, 
              'and Your Current Account number is ', self.balance)
        
    def withdrawal(self):
        print('Your previous Balance is = ', self.balance)
                
        withdraw = int(input('How much you want to withdrawal = '))
        if withdraw <= self.balance: 
            self.balance -= withdraw
            print('SBI Bank Rs. ',withdraw, 'withdrawn from your Account No ', self.acc_number, 
              'and Your Current Account number is ', self.balance)
        else:
            print("\n Alert: Helloooo Boss, You don't have sufficient balance")                          
        
        
        


# In[35]:


bank_details = User_Account(12345,0)


# In[36]:


bank_details.login()


# In[37]:


bank_details.user_details()


# In[39]:


bank_details.deposite()


# In[40]:


bank_details.withdrawal()


# ### Encapsulation
# 
# Encapsulation is an another powerful way to extend a class which consists on wrapping an object withsecond one.

# In[6]:


class Tyre:
    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure
        
    def __str__(self):             # __str__ can be used if you don want to define a method name but you want this to excute.
        return ("Tyres: \n \tBranch: " + self.branch +
               "\n \tBelted-bias: " + str(self.belted_bias) +   # __str__ returns only text so we are converting into string
               "\n \tOptimal Pressure: " + str(self.opt_pressure))
    

class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level

    def __str__(self):
        return ("Engine: \n \tFuel_Type: " + self.fuel_type +
                "\n \tNoise Level: "+ str(self.noise_level))

class Body:
    def __init__(self, size):
        self.size =size

    def __str__(self):
        return ("Body: \n \tSize: " + self.size)

class Car:
    def __init__(self, tyre, engine, body):
        self.tyre = tyre
        self.engine = engine
        self.body = body
    
    def __str__(self):
        return str(self.tyre) + '\n' + str(self.engine) + '\n' + str(self.body)
    
t=Tyre('MRF', True, 34)
e=Engine('Petrol', 2.3)
b=Body('SUV')

c= Car(t, e, b)
print(c)


# In[ ]:




