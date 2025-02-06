import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'salary': [50000, 60000, 70000]
})

# Select all employees
df

# Select specific columns
df[['name', 'salary']]

# Select rows where salary is greater than 50000
df[df['salary'] > 50000]

# Select rows where name is not null
df[df['name'].notna()]

# Select all employees ordered by salary in descending order
df.sort_values(by='salary', ascending=False)

# Count the number of employees
df.shape[0]

# Select the average salary by department
df.groupby('department')['salary'].mean()

# Select all employees and their departments
df.merge(departments, on='department_id')