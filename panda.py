import pandas as pd
# student data has student_id and age
student_data = [
    { 
        'student_id': 1,
        'age': 15
    },
     { 
        'student_id': 2,
        'age': 11
    },
     {
        'student_id': 3,
        'age': 11
    },
     { 
        'student_id': 4,
        'age': 20
    }
]
print('student_data',student_data)
student_datapd = pd.DataFrame(student_data)
print('student_datapd')
print(student_datapd)


print('-----')


# Write a solution to calculate and display the number of rows and columns of players.

# Return the result as an array:

# [number of rows, number of columns]


# 2.import pandas as pd

dframe = {'player_id': [846,749,155,583,388,883,355,247,761,642],
          'name': ['Mason','Riley','Bob','Isabella','Zachary','Ava','Violet','Thomas','Jack','Charie'],
          'age': [21,30,28,32,24,23,18,27,33,36] ,
          'position':['Forword','Winger','Striker','GoalKeeper','Midfielder','Defender','Striker','Striker','MidFielder','Center-Back'],
          'Team':['ReadMadrid','Barcelona','Mancherunited','Liveerpool','BayernMunich','Chelsea','Juventus','Parissaint','Manchestercity','Arsenal']
          }

players=pd.DataFrame(dframe)

print()
print(players.shape)

print('---')

# Write a solution to display the first 3 rows of this DataFrame.

# 3.import pandas as pd
dframe = { 
          'employee_id' : [3,90,9,60,49,43],
          'name' : [ 'Bob','Alice','Tatiana','Annabelle','Jonathan','Khaled'],
          'department' : ['Operations','Sales','Engineering','Information Technology','HumanResourses','Administration'],
          'salary': [48675,11096,33805,37678,23793,40454] 
         }

employee=pd.DataFrame(dframe)
print(employee.head(3))

# 4.
import pandas as pd

dframe= {
    'student_id': [101,53,128,3],
    'name': ['ulysses','William','Henry','Henry'],
    'age': [13,10,6,11]
}

students = pd.DataFrame(dframe)
result = students[students['student_id'] == 101][['name', 'age']]
print(result)

# 5
import pandas as pd

# Sample data
data = {
    'employee_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'salary': [50000, 60000, 70000]
}

# Create the DataFrame
employees = pd.DataFrame(data)

# Create the new 'bonus' column
employees['bonus'] = employees['salary'] * 2

# Display the updated DataFrame
print(employees)

# 6.
import pandas as pd

# Sample data
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': [
        'emily@example.com',
        'michael@example.com',
        'sarah@example.com',
        'john@example.com',
        'john@example.com',  # Duplicate email
        'alice@example.com'
    ]
}
# Create the DataFrame
customers = pd.DataFrame(data)

# Remove duplicate rows based on the 'email' column, keeping only the first occurrence
customers_data = customers.drop_duplicates(subset='email', keep='first')

# Display the result
print(customers_data)

# 8.
import pandas as pd
data = {
    'student_id': [32, 217,779,849],
    'name': ['Piper','none','Georgia','Willow'],
    'age' : [ 5, 19,20,14]
}
students = pd.DataFrame(data)
print(students)
students_data =students.dropna()
print(students_data)

# 9.

import pandas as pd
data = {
    'name': ['Jack','Piper','Mia','Ulysses'],
    'salary':[19666,74754,62509,54866]
}

employees = pd.DataFrame(data)
print("original Dataframe:")
print(employees)

employees['salary'] = employees['salary'] * 2
print("\nModified DataFrame with doubled salaries:")
print(employees)

# 10.
import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5],
    'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age': [6, 7, 16, 18, 10]
}

students = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(students)

# Rename the columns
students.rename(columns={
    'id': 'student_id',
    'first': 'first_name',
    'last': 'last_name',
    'age': 'age_in_years'
},inplace=True)

# Display the modified DataFrame
print("\nModified DataFrame with renamed columns:")
print(students)



# 11
import pandas as pd
data = {
    'id': [1,2,3,4,5],
    'first': ['Mason','ava','taylor','georgia','thomas'],
    'last':['king','wright','hall','thompson',
     'moore'],
    'age': [6,7,16,18,10]
}
df = pd.DataFrame(data)
df.rename(columns={
    'id':'student_id',
    'first':'first_name',
    'last': 'last_name',
    'age':'age_in_years'},
     copy=True)
print(df)


# 12.
import pandas as pd

data = {
    'student_id': [1,2],
    'name':['Ava','Kate'],
    'age':[6,15],
    'grade':[73.0,87.0]
}
df = pd.DataFrame(data)
print(df)
df['grade']=df['grade'].astype (int)
print(df)

13.
import pandas as pd
data = {
    'name':['wristwatch','wirelessearbuds','golfclubs','printers'],
    'quantity': ['none','none',779,849],
    'price': [135,821,9319,3051],
}
df = pd.DataFrame(data)
print(df)
df['quantity'] = pd.to_numeric(df['quantity'].replace('none',pd.NA))
df['quantity'].fillna(0,inplace = True)
print(df)

# 14.
import pandas as pd

# Sample DataFrame df1
data1 = {
    'student_id': [1, 2, 3, 4],
    'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
    'age': [8, 6, 15, 17]
}
df1 = pd.DataFrame(data1)

# Sample DataFrame df2
data2 = {
    'student_id': [5, 6],
    'name': ['Leo', 'Alex'],
    'age': [7, 7]
}
df2 = pd.DataFrame(data2)

# Concatenate df1 and df2 vertically
df_concatenated = pd.concat([df1, df2])

# Display the concatenated DataFrame
print(df_concatenated)

# 15.
import pandas as pd
data = {
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville',
             'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month':['January', 'February', 'March', 'April', 'May',
              'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
}
df = pd.DataFrame(data)

pivoted_df = df.pivot(index = 'month',columns= 'city',values = 'temperature')
print(df)