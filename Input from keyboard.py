#!/usr/bin/env python
# coding: utf-8

# In[3]:


rows = int(input('Enter the number '))
#rows = 7
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')


# In[2]:


rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')


# In[6]:


rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(i, end=' ')
    print('\r')


# In[3]:


name = input('Enter your name = ')

if name.isalpha():
    print('you entered ', name )
else:
    print('enter only alphabet')
        


# In[4]:


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
                


# In[7]:


car_yrs = int(input('Enter the car manufacturing year '))
car_km = int(input('Enter the car Kilometer '))
car_name = input('the the brand ')

used_car_info(car_yrs, car_name,car_km)

