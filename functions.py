#!/usr/bin/env python
# coding: utf-8

# In[3]:


def say_hello():
    print('this is a simple example of defing function')


# In[4]:


say_hello()


# In[5]:


def greeting(name):
    print('Hello', name)


# In[7]:


greeting('I am doing a data science course')


# ### Using return
#  Return allowa a function to "return" a result that can be stored as a variable, or used in whatever manner a user wants.
#  
# #### Salary Update example

# In[8]:


# without return

def Salary_Incr(Fixed_sal, house_rent):
    total_sal= Fixed_sal + house_rent
    
    if total_sal<=9000:
        total_sal + 1000
    else:
        total_sal
        


# In[12]:


print('The new sal =' , Salary_Incr(6500,2000))


# In[13]:


# with return

def Salary_Incr(Fixed_sal, house_rent):
    total_sal= Fixed_sal + house_rent
    
    if total_sal<=9000:
        return total_sal + 1000
    else:
        return total_sal
        


# In[18]:


print('The new sal =' , Salary_Incr(6500,2000)) 


# In[34]:


def used_car_info(car_yrs, car_name,car_km):
    if car_yrs == 2021:
        if car_km >= 10000 and car_km <= 15000:
            if car_name == 'Hyundai Creta':
                print('Hyundai Car price is = 900000 to 1050000')
            else:
                print('this time car is not available')
        
        elif car_km >= 16000 and car_km <= 20000:
            if car_name == 'Honda Amaze':
                print('Honda Car price is = 600000 to 800000')
            else:
                print('this time car is not available')
        else:
            print('No stock right now')
    elif car_yrs == 2020:
        if 12000 < car_km < 16000:
            if car_name == 'Maruti swift':
                print('Maruti Car price is = 555000 to 600000')
            else:
                print('this time Maruti car is not available')
        elif 15000 < car_km < 20000:
            if car_name == 'ford figo':
                print('ford Car price is = 355000 to 500000')
            else:
                print('ford Not avail')
        else:
            print('out of stock')
    else:
        print('not available below 2020 years')  
                
    


# In[40]:


used_car_info(2019, 'ford', 21000)


# ### Lambda function
# 

# In[41]:


# Syntax - lambda arguments : expression

add_num = lambda x : x + 30
print(add_num(70))


# In[42]:


multi_num = lambda x, y : x * y
print(multi_num(5,10))


# ### * *args and  *** kwargs
# 

# In[50]:


# *args takes multiple inputs

def my_func(*args):
    x=0
    for i in args:
        x += 1 
        print('My', x, 'arg is-', i)    


# In[51]:


my_func('vikas', 1, 100, 35.5, 'sharma')


# In[57]:


def my_kwarg(**kwargs):
    for key, value in kwargs.items():
        
        print(key, '=', value)    


# In[61]:


my_kwarg(student=['Vikas, Aarti'], Marks= [78,70], age=[32,30])


# In[59]:


get_ipython().system('pip3 install jedi==0.17.2')


# ### map()
# 
# map is a function which will returnupon iterating over set of elements(tuple, list,etc).it is used when you want to apply a single transformation function to all the iterable elements.
# 
# Syn- map(function,sequence)

# In[8]:


# prog logic is that when we have no. of student marks and some of students got the marks
# which is the boundary of passing marks then where we can use map function.

def grace_marks(marks):
    if marks == 33:
        return marks + 2
    elif marks == 32:
        return marks + 3
    else:
        return marks


# In[9]:


marks =[52,32,48,45,33,50,35,33]


# In[10]:


total = list(map(grace_marks, marks))

print(total)


# In[11]:


total.count(35)


# ### filter()
# 
# filter is a function which offers a convenient way to filter out all the elements of an iterable, for which the function returns "True" that means Only TRUE value is returned.
# 
# Syn- filter(function,sequence)

# In[13]:


#print those student marks who failed
def filter_marks(marks):
    if marks < 35:
        return marks


# In[14]:


marks = [35,55,30,32,45,31]


# In[15]:


failed = list(filter(filter_marks, marks))


# In[16]:


failed


# ### Difference between map and filter
# 
# Map accepts all elements in a given list and a function can be applied to it.
# 
# Filter accepts all data in a list and runs that through a function to create a new list with all elements that return True in that function

# In[22]:


list(map(lambda var: var%2 == 0, [1,2,3]))


# In[23]:


list(filter(lambda var: var%2 == 0, [1,2,3]))


# ###  Global & Local variable
# 

# In[24]:


# Global variable defined outside the function. This variale can be used outside as well as inside the function.
# if you want to use variable anywhere inthe program you can use global variable.

extra_marks = 10

def tot_score_glob():
    print('Printing inside the function and total is', 35 + extra_marks)

tot_score_glob()


# In[25]:


print('Printing inside the function and total is', 35 + extra_marks)


# In[26]:


# local variable defined inside the function. This variale can be used only inside the function.
# if you want to restrict the variable usage within the function itself  and don't want to use anywhere outside 
# the fnction then use local variable. 

def tot_score_local():
    some_marks = 10
    print('Printing inside the function and total is', 35 + some_marks)

tot_score_glob()


# In[28]:


print('Printing inside the function and total is', 35 + some_marks)


# ### How to use local variable outside the variable
#  it is possible when we make a local variable into a global variable using keyword "global"

# In[33]:


def local_global():
    global x
    x= 10
    print('the value of x =', x)

local_global()


# In[35]:


print(x)

