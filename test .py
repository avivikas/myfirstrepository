#!/usr/bin/env python
# coding: utf-8

# 1- company employee getting salary as 22500, 50005, 45000, 19350, 25000, 10250, 15505. Write a pogram to store only those salary which are less than 25000 and display all the saved salary.

# In[1]:


salary = [22500, 50005, 45000, 19350, 25000, 10250, 15505]
salary


# In[2]:


less_sal = []
for sal in salary:
    if sal < 25000:
        less_sal.append(sal)
        print(less_sal) # adding salary to list
    


# In[3]:


print(less_sal)


# 2- In a start up company one of the employee foget his salaty and request to HR to tell hos salary. Write a program to fetch only Rohit's salary and print below output from your python code.
# 
# ### Dear Rohit your salary is 5000
# 
# Employee salary and their salary respectively.
# 
# - emp_sal = [2000,4000,5000,6000,6500,5200]
# - emp_name = ['Farhad', 'Shankar', 'Rohit', 'Astha', 'Shital', 'Abhishek']

# In[5]:


emp_sal = [2000,4000,5000,6000,6500,5200]
emp_name = ['Farhad', 'Shankar', 'Rohit', 'Astha', 'Shital', 'Abhishek']

for val in emp_name:
    if val == 'Rohit':
        name_index = emp_name.index(val) #nIdentifying the Index Number using index method
        print("Dear", val, "your salary is-", emp_sal[name_index]) # Using the index numebr fetching the name


# Write a pytho code to calculate health premium. Accept data from user through input keyboard and use function
# 
# 1- GENDER- male and female only
# 
# 2-DATE OF BIRTH - year only (no date and month)
# 
# 3-SMOKER - yes and no only
# 
# premium criteria should be-
# 
# 1- For MALE born between 1990-2000 and if he is a smoker, print as "Your annual premium is Rs.35000" and for NOM SMOKER apply discount 10% TO 35000 and print final discounted price.
# 
# 2- if born between 1970-1990 and smoker, premium is Rs.40000" and for NOM SMOKER apply discount 5% TO 40000 and print final discounted price.
# 
# 3- For FEMALE born between 1990-2000 and if he is a smoker, print as "Your annual premium is Rs.30000" and for NOM SMOKER apply discount 10% TO 30000 and print final discount ed price.
# 
# 4- if born between 1970-1990 and smoker, premium is Rs.35000" and for NOM SMOKER apply discount 5% TO 35000 and print final discounted price.

# In[11]:


def cal_health_pre(gender, dob, smoker):
    if gender == 'm':
        if dob >= 1990 and dob <= 2000:
            if smoker == 'yes':
                print('Your premium is 35000')
            else:
                prem= 35000 - (35000 * 0.1)
                print('your premium is ', prem)
        
        elif dob >= 1970 and dob <= 1990:
            if smoker == 'yes':
                print('Your premium is 40000')
            else:
                prem= 40000 - (40000 * 0.05)
                print('your premium is ', prem)
        else:
             print('he is not born in above years')
                
    elif gender == 'f':
        if dob >= 1990 and dob <= 2000:
            if smoker == 'yes':
                print('Your premium is 30000')
            else:
                prem= 30000 - (30000 * 0.1)
                print('your premium is ', prem)
        
        elif dob >= 1970 and dob <= 1990:
            if smoker == 'yes':
                print('Your premium is 35000')
            else:
                prem= 35000 - (35000 * 0.05)
                print('your premium is ', prem)
        else:
             print('She is not born in above years')        
        


# In[23]:


gender = input("Enter the gender -")
dob = int(input('Enter the DOB -'))
smoker = input("Enter He/She is smoker or not - ")


# In[24]:


cal_health_pre(gender,dob,smoker)


# In[ ]:





# In[ ]:




