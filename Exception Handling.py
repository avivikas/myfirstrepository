#!/usr/bin/env python
# coding: utf-8

# ### Errors and Exception handing
# In this section, we will learn about Errors and exception handing in python. you have might definitely encountered errors.
# 
# ### try and except
# syntax-
# 
# try:
# 
#     you do your operatons here...
# 
# except Exceptiona1:
# 
#      if there is Exception1, then excute this block.
# 
# except Exceptiona2:
# 
#      if there is Exception2, then excute this block.
#      
#      .....
# else:
# 
#       if there is no exception, then excute this block.   

# In[1]:


mark1 = 25

subject = 'Data Science'

mark2 = 35


# In[2]:


try:
    total_marks = mark1 + subject
    
except TypeError:
    print('you are adding integer to string. Make sure both data type are matching')
    
else:
    print('Total marks = ', total_marks)


# In[3]:


try:
    total_marks = mark1 + mark2
    
except TypeError:
    print('you are adding integer to string. Make sure both data type are matching')
    
else:
    print('Total marks = ', total_marks)


# In[2]:


try:
    car_number = input('\n Enter the Car Number ')
    cust_name = input('\n Enter the owner name  ')
    mobile = input('\n Enter the Mob. No. ')
    
    if car_number == '':
        raise Exception()
    elif cust_name == '':
        raise Exception()
    elif mobile == '':
        raise Exception()
    else:
        pass

except:
    # For Car number
    if car_number == '':
        print('\n The car number field is required ')
        
    # for owner name
    if cust_name == '':
        print('\n The owner name field is required')
        
    # for mobile number
    if mobile  == '':
        print('\n The mobile number field is reqired')
    
# else part will excute only when there is no issue with try block
else:
    print('\n thanks for all the details')
    


# ### finally: block
# 
# Now we don't actually need to memorize the list of exception types! Now what if we keep wanting to run code after the exception occured?This is where Finally comes in.
# the finally block of code will always be rum regardless if there was an exception in the try code block.

# In[2]:


try:
    car_number = input('\n Enter the Car Number ')
    cust_name = input('\n Enter the owner name  ')
    mobile = input('\n Enter the Mob. No. ')
    
    if car_number == '':
        raise Exception()
    elif cust_name == '':
        raise Exception()
    elif mobile == '':
        raise Exception()
    else:
        pass

except:
    # For Car number
    if car_number == '':
        print('\n The car number field is required ')
        
    # for owner name
    if cust_name == '':
        print('\n The owner name field is required')
        
    # for mobile number
    if mobile  == '':
        print('\n The mobile number field is reqired')
    
# finally block excute all the time. 
finally:
    print('\n In any case filnally block will excute')


# In[15]:


def mobile_no():
    try:
        mob= int(input('Enter the mobile number '))
    
    except:
        print('Look like you did not enter the integer number')
    
    print('You entered ', mob)


# In[17]:


mobile_no()


# check how we got an error when trying to print mob(because it was properly assigned). Let's find the right solution by asking the user and ckecking to make sure the input type is an integer

# In[18]:


x = 9889986790


# In[19]:


len(x)


# In[20]:


len(str(x))


# In[25]:


def mob_num():
    
    while True:
        try:
            mob= int(input('Enter the mobile Number  \n')) # if it is not integer control will jump into the except block.
            
            if len(str(mob)) != 10:
                print('\n Mobile number must be 10 digit \n')
                continue
            else:
                print('\n Thank You')
                break
        except:
            print('\n Look like you did not enter an integer! \n')
            continue


# In[26]:


mob_num()


# In[ ]:




