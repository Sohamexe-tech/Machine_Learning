import pandas as pd

data={
	'Name':   ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
	'Age':    [25, 30, 35, 28, 22],
	'Salary': [50000, 70000, 90000, 60000, 45000],
	'Dept':   ['HR', 'Eng', 'Eng', 'HR', 'Design']
}
df = pd.DataFrame(data)
print(df)

print(df.shape)         
print(df.dtypes)        
print(df.describe())    
print(df.info())      
print(df.head(3))      
print(df.tail(2)) 

print(df['Age'])                     
print(df[['Name', 'Salary']])        

print(df.loc[0])                     
print(df.loc[1:3, 'Name':'Salary'])  
print(df.iloc[0])                    
print(df.iloc[0:2, 0:3]) 

print(df[df['Age'] > 27])                         
print(df[(df['Age'] > 25) & (df['Dept'] == 'Eng')]) 
print(df[df['Dept'].isin(['HR', 'Design'])])       

# --- Adding / Modifying Columns ---
df['Salary_K'] = df['Salary'] / 1000          # new column
df['Senior']   = df['Age'] > 28               # boolean column
df['Bonus']    = df['Salary'].apply(lambda x: x * 0.1)  # apply function

# --- Handling Missing Data ---
df2 = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, 8]})

print(df2.isnull().sum())       # count nulls per column
df2.fillna(0, inplace=True)     # fill with 0
df2.fillna(df2.mean(), inplace=True)  # fill with column mean
df2.dropna(inplace=True)        # drop rows with any null   

# --- GroupBy (SQL-style aggregation) ---
print(df.groupby('Dept')['Salary'].mean())    # avg salary per dept
print(df.groupby('Dept').agg({'Salary': 'mean', 'Age': 'max'}))              