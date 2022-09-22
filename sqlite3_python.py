#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python

import sqlite3

# connecting with the database(if there is no database exist, It will create one).
db = sqlite3.connect("student_database.db")


# In[2]:


# Declare cursor
cursor = db.cursor()


# In[ ]:


# Create table
cursor.execute("create table student_data(phone_no INT Primary Key, email_id TEXT, Course_name TEXT, Fee_paid INT)")


# In[7]:


# insert records into the table 
cursor.execute("Insert into student_data(phone_no, email_id, Course_name, Fee_paid) values (9805585458, 'amar@gmail.com', 'data science', 55000)")

# save the records permanently.(If you don't commit, next time you will not see the records in the table)
db.commit()

# count the records inserted
print(cursor.rowcount, "Record(s) inserted")


# ### SELECT query - How to fetch records from the table

# In[8]:


# insert records into the table 
cursor.execute("Insert into student_data(phone_no, email_id, Course_name, Fee_paid) values (9805585451, 'rahul@gmail.com', 'data science', 55000)")

# save the records permanently.(If you don't commit, next time you will not see the records in the table)
db.commit()

# count the records inserted
print(cursor.rowcount, "Record(s) inserted")


# In[10]:


result= cursor.execute("SELECT * FROM student_data")
for row in result:
    print(row)


# In[16]:


cursor.execute("insert into student_data values(9889986798, 'littleone@gmail.com','cloud software',58000)")
db.commit()

print(cursor.rowcount, "Record(s) inserted")


# In[17]:


# multiple records insertion
cursor.execute("insert into student_data values(9889986584, 'theone@gmail.com','cloud architect',60000),(9889747744, 'mlb@gmail.com','data science',60000)")
db.commit()

print(cursor.rowcount, "Record(s) inserted") 


# In[18]:


result= cursor.execute("SELECT * FROM student_data")
for row in result:
    print(row)


# ### How to load data from file into table
# 
# Note :- keep csv file the same folder where your jupyter notebook is provide folderlink. You cannot open file directly from github
# 
# https://github.com/training-ml/Files  - this is the link from where we access the data science materials

# In[19]:


with open('DT_Students.csv','r') as file:
    no_record =0
    for row in file:
        cursor.execute("insert into student_data values ( ?, ?, ?, ?)",row.split(","))
        db.commit()
        no_record +=1
print(no_record, "Record(s) Inserted")


# In[20]:


result= cursor.execute("SELECT * FROM student_data")
for row in result:
    print(row)


# ### where clause - select records based on condition

# In[23]:


sql = "Select * from student_data WHERE course_name = 'Data Science' or course_name = 'data science'"
result = cursor.execute(sql)
for row in result:
    print(row)


# In[24]:


sql = "Select * from student_data WHERE fee_paid >= 50000 "
result = cursor.execute(sql)
for row in result:
    print(row)


# ### DELETE record - how to delete unwanted records.
# Usually developer/Data Scientists are not authorized to delete any records from the table. Database Admin does this kind of tasks

# In[25]:


sql = "DELETE from student_data WHERE phone_no = 9889585458 "

result = cursor.execute(sql)
db.commit()


# In[26]:


result= cursor.execute("SELECT * FROM student_data")
for row in result:
    print(row)


# In[29]:


sql = "Select * from student_data"
result = cursor.execute(sql)
for row in result:
    print(row)


# In[31]:


sql = "DELETE from student_data WHERE course_name = 'data science' "

result = cursor.execute(sql)
db.commit()


# In[32]:


result= cursor.execute("SELECT * FROM student_data")
for row in result:
    print(row)


# ### ORDER BY

# In[37]:


# How to change the order of record (Increasing or decreasing)
result= cursor.execute("SELECT * FROM student_data order by fee_paid")
for row in result:
    print(row)


# In[38]:


result= cursor.execute("SELECT * FROM student_data order by fee_paid desc")
for row in result:
    print(row)


# ### UPDATE Table- Update the column value

# In[39]:


# Single Record update
cursor.execute("UPDATE student_data SET course_name= 'Cloud Architect' where fee_paid = 140000")


# In[40]:


result= cursor.execute("SELECT * FROM student_data")
for row in result:
    print(row)


# In[41]:


result= cursor.execute("SELECT * FROM student_data order by fee_paid")
for row in result:
    print(row)


# In[42]:


result= cursor.execute("SELECT * FROM student_data where fee_paid = 140000")
for row in result:
    print(row)


# In[44]:


#multiple ecords update using 'IN'
cursor.execute("update student_data SET fee_paid = 135000 where phone_no IN(9889986584, 9988776609, 9988776610)")


# In[46]:


result= cursor.execute("SELECT * FROM student_data where phone_no IN(9889986584, 9988776609, 9988776610)")
for row in result:
    print(row)


# In[5]:


result= cursor.execute("SELECT * FROM student_data order by phone_no desc")
for row in result:
    print(row)


# In[7]:


# update the records using BETWEEN
sql = "Update student_data set course_name = 'Tableau' where phone_no between 9988776605 and 9988776608"
cursor.execute(sql)

# Verify if its updated
result= cursor.execute("SELECT phone_no, course_name FROM student_data where course_name ='Tableau'")
for row in result:
    print(row)


# ### MIN nad MAX Function

# In[9]:


result= cursor.execute("SELECT MIN(fee_paid) FROM student_data")
print("Minimum Fee = ", result.fetchone())


# In[12]:


result= cursor.execute("SELECT MAX(fee_paid) FROM student_data")
print("Minimum Fee = ", result.fetchone())


# ### Subquery
# In SQL, A query within another query is called subquery. In other word we can say that a Subquery is a query that is embedded in WHERE clause of another SQL query.
# Subqueries can be used with SELECT,UPDATE, INSERT,DELETE statements along with expression operator.

# In[4]:


import sqlite3
db = sqlite3.connect("student_course_database.db")


# In[5]:


cursor = db.cursor()


# In[6]:


cursor.execute("create table course1(courseid INT Primary Key, coursename TEXT, duration INT)")


# In[ ]:


cursor.execute("create table student1(rollno INT Primary Key, studentname TEXT, age INT, courseid int, foreign key(courseid) references course1(courseid))")


# In[10]:


cursor.execute("insert into course1 values (78, 'Data Science', 12),(56, 'python', 4),(101, 'Database', 7)")
print(cursor.rowcount, "recors(s) inserted")

db.commit;


# In[11]:


cursor.execute("insert into student1 values (1, 'vikas', 30, 78),(2, 'tabrez', 30, 56),(3, 'nupriya', 29, 78),(4, 'bhuwnesh',32,56)")
print(cursor.rowcount, "recors(s) inserted")

db.commit;


# In[12]:


result= cursor.execute("select * from course1")
for row in result:
    print(row)


# In[13]:


result= cursor.execute("select * from student1")
for row in result:
    print(row)


# In[18]:


result= cursor.execute("select * from student1 where courseid=(select courseid from course1 where coursename = 'Data Science')")
result.fetchall()


# In[19]:


result= cursor.execute("select * from student1 where courseid=(select courseid from course1 where coursename = 'python')")
result.fetchall()


# In[20]:


result= cursor.execute("select * from student1 where courseid=56")
for row in result:
    print(row)


# In[21]:


result= cursor.execute("select * from student1 where courseid=(select courseid from course1 where coursename = 'python')")
for row in result:
    print(row)


# ### JOIN
# 1- INNER JOIN - Return record that have matching values in both tables
# 
# 2- LEFT JOIN - Return all record from the left table, and matched record from the right table.
# 
# 3- RIGHT JOIN - Return all record from the right table, and matched record from the left table. 
# 
# 4- FULL JOIN - Return all records when there is a match in either left or right table

# In[11]:


cursor.execute("create table student3(phone_no INT Primary Key, student name TEXT, enrolled_date TEXT, marks INT)")


# In[13]:


with open('Students_details.csv','r') as file:
    no_record =0
    for row in file:
        cursor.execute("insert into student3 values ( ?, ?, ?, ?)",row.split(","))
        db.commit()
        no_record +=1
print(no_record, "Record(s) Inserted")


# In[14]:


result= cursor.execute("select * from student3")
for row in result:
    print(row)


# ### INNER JOIN

# In[16]:


sql = "select student_data.phone_no, student3.enrolled_date, student3.marks from student_data INNER JOIN student3 ON student_data.phone_no = student3.phone_no"
result = cursor.execute(sql)
for row in result:
    print(row)


# ### LEFT JOIN

# In[ ]:


sql = "select student_data.phone_no, student3.enrolled_date, student3.marks from student_data LEFT JOIN student3 ON student_data.phone_no = student3.phone_no"
result = cursor.execute(sql)
for row in result:
    print(row)


# #### RIGHT JOIN and FULL OUTER JOIN not suppoted in Sqlite3 

# ### PYTHON and SQL (How to deal with python code

# In[3]:


while True:
    
    try:
        ph_num =int(input("Enter your mobile number  "))
        
        if len(str(ph_num))!= 10:
            print("Enter the 10 digit phone number")
            continue
        else:
            result = cursor.execute("select * from student3")
            for detail in result:
                if detail[0] == ph_num:
                    print('Name = ', detail[1])
                    print('Enrolled Date = ',detail[2])
                    print('Mark = ',detail[3])
                    break
            else:
                print("Phone Number not found in database")
                break
#            continue
            break
    except:
        print("Phone number should be numeric")
        continue

