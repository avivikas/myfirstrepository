#!/usr/bin/env python
# coding: utf-8

# In[1]:


Marks= 34

if Marks >= 60:
    if Marks > 70: 
        print(Marks, "-Dictiction")
    else:
        print(Marks, "-first")
    
elif Marks >50 and Marks<=59:
        print(Marks, "-Second")
    
elif Marks >=35:
        print(Marks, "-Pass")
    
else:
        print(Marks, "-Fail! Better luck next")
    


# ### Set items are unordered, unchangeable, and do not allow duplicate values

# In[2]:


num = set()


# In[3]:


num


# In[4]:


num= set(1)


# In[5]:


num.add(1)


# In[6]:


num


# In[7]:


type(num)


# In[8]:


num.add(2)
num.add(4)
num.add(1)
num.add(5)
num


# In[9]:


num.add(3)
num


# In[10]:


L=[6,3,6,1,2,5,4,9,8,1,3,4,5,7]
L


# In[11]:


rem_dupli= set(L)


# In[12]:


rem_dupli


# In[13]:


name= set('Vikas', 'Aarti' , 'Raj', 'Virat', 'Arti', 'Aarti')
name


# In[14]:


name= set('Vikas')
name


# In[15]:


name.add('r')
name


# In[16]:


name.pop(0)
name


# In[17]:


name.pop()
name


# In[18]:


name.add("vikas")
name


# In[19]:


name1 = {'vikas', 'ajay', 'tabbu'}
name1


# In[20]:


type(name1)


# In[21]:


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


# In[22]:


set1


# In[23]:


set3


# In[24]:


set2


# In[25]:


set1
set2
set3


# In[27]:


name= set('Vikas', 'Aarti' , 'Raj', 'Virat', 'Arti', 'Aarti')
name


# In[31]:


name= set(('Vikas', 'Aarti' , 'Raj', 'Virat', 'Arti', 'Aarti'))
name


# In[29]:


name.pop()
print(name.pop())


# In[32]:


name


# In[33]:


name.pop()
name


# In[34]:


name.pop()
print(name.pop())


# In[35]:


name


# In[1]:


#          Creating Dictionary

my_dic ={'Roll_no' : 3, 'marks' : [78,85,68], 'sub': ['math', 'science','computer']}
my_dic


# In[8]:


'Roll_no'


# In[9]:


my_dic['sub']


# In[14]:


my_dic['Roll_no']


# In[16]:


my_dic['marks'][1]


# In[23]:


my_dic['marks']


# In[24]:


my_dic['sub'][2]


# In[25]:


my_dic['sub'][1].upper()


# In[29]:


my_dic['marks'].sort()
my_dic['marks']


# In[30]:


my_dic['marks'].reverse()


# In[31]:


my_dic['marks']


# In[ ]:


my_dic['sub'].


# In[32]:


my_dic


# In[33]:


# lengthy code to add marks to the data of the list
my_dic['marks'][1] = my_dic['marks'][1] + 2


# In[34]:


my_dic['marks'][1]


# In[35]:


my_dic


# In[36]:


# Sort code to add number to the data of the list
my_dic['marks'][2]+= 2


# In[37]:


my_dic


# In[39]:


my_dic['marks'][0] -= 3
my_dic


# In[40]:


# To add new key in exist dictionary
my_dic['year'] = '2nd'


# In[41]:


my_dic


# In[42]:


# update value
my_dic['sub'][0] = 'english'


# In[43]:


my_dic


# In[44]:


my_dic.items()


# In[46]:


my_dic


# In[47]:


final_dic= my_dic.copy()


# In[48]:


final_dic


# In[49]:


my_dic.keys()


# In[50]:


my_dic.values()


# In[ ]:


my_dic.


# In[51]:


# Update value of dictionary by update mathod
my_dic.update({'Roll_no' : 1})


# In[52]:


my_dic


# In[7]:


i = 1
while i < 6:

  print(i)
  i += 1


# ## for loop-
#  for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# In[8]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# ## Looping Through a String
#  Even strings are iterable objects, they contain a sequence of characters:

# In[9]:


for x in "banana":
  print(x)


# ## The break Statement
#  With the break statement we can stop the loop before it has looped through all the items.
# The braek statement terminate the loop containing it.

# In[10]:



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


# In[12]:


for x in fruits:
  if x == "banana":
    break
  print(x)


# In[36]:


# table program using nested for loop

for x in range(2,6):
    print("table of", x)
    for y in range(1,11):
        print(x, 'x',y, '=', x * y)
        if y == 10: 
            print('\n')
            


# In[39]:


for x in range(2,6):
    print("table of", x)
    for y in range(1,11):
        print(x, 'x',y, '=', x * y)
        if y == 10: 
            print('\n')


# In[3]:


n=int(input("Enter the number to print the tables for:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)


# In[ ]:





# In[45]:


item1 = 200

item2 = 200

if (item1 + item2) >= 500:
    print("you are eligible for free shipping")

else:
     extra = 500 - (item1 + item2)
     print(" you have to purchase", extra, "Rs worth of an item for free shipping")


# In[46]:


# range()function

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and stops before a specified number.

# Syntax
# range(start, stop, stepsize)

print(range(10))


# In[47]:


print(list(range(10)))


# In[49]:


roll_number = list(range(1,8))
roll_number


# In[51]:


step_size = list(range(1,22,2))
step_size


# In[16]:


reverse = list(range(10,2,-1))
reverse


# In[ ]:


# range fuction dont work for flaot data. we can fix this issue in the numpy classes


# In[19]:


# While Loop while loop in pythone is used to iterate overa block of code as long as the test expression(condotion) is true.
i= 0
 
while i < 10:
    i = i + 1
    print(i, 'Data Science')


# In[4]:


import time
curr_time = time.localtime()
print(curr_time)


# In[6]:


# let'say you have set an alarm and how this works?

while True:
    curr_time = time.localtime()
    if curr_time.tm_hour == 19 and curr_time.tm_min == 10:
        print("wake up my son")
        break
    


# In[ ]:


# Difference between for loop and while loop
# for loop- if you know how many times you want to excute the code then we use for loop.
# Wile loop- if you don't know how many times you want to excute the code then we use while loop with condition.


# In[10]:


# Enumerate() allow us to itrate through a sequence but it keeps track of both tha index and the element.

stu_name = ['Vikas', 'Aarti', 'Avi', 'Mummy','Papa']
for name in enumerate(stu_name):
    print(name)


# In[12]:


set1 = {1, 2, 3, 4, 5}
print(set(enumerate(set1)))


# In[24]:


set2 = {"H", "e", "l", "l", "o"}
L1= list(set2)
for i in enumerate(L1):
    print(i)


# In[25]:


stu_name = ['Vikas', 'Aarti', 'Avi', 'Mummy','Papa']
for name in enumerate(stu_name,2):
    print(name)


# In[26]:


# Zip

stu_name = ['Vikas', 'Aarti', 'Avi', 'Mummy','Papa']
stu_mark = [88, 98, 55, 89, 53]


# In[28]:


student_details = list(zip(stu_name, stu_mark))
student_details


# In[29]:


# Unzip

name , marks = zip(*student_details)


# In[30]:


name


# In[31]:


marks


# In[32]:



# The break Statement
# With the break statement we can stop the loop before it has looped through all the items.
# The braek statement terminate the loop containing it.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


# ### The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
# 
# 

# In[13]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
    continue
    print(x)


# In[15]:


i = 0
while i < 9:
    i += 1
    if i == 3:
        continue
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




