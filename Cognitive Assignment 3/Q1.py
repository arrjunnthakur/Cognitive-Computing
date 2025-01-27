import pandas as pd
data = {
    "tid": [1, 2, 3, 4, 5,6,7,8,9,10],
    "refund": ["Yes", "No", "No", "Yes", "No","No","Yes","No","No","No"],
    "marital status": ["Single", "Married", "Single", "Married", "Divorced","Married","Divorced","Single","Married","Single"],
    "taxable income": ["125K", "100K", "70K", "120K", "95K","60K","220K","85K","75K","90K"],
    "cheat": ["No", "No", "No", "No", "Yes","No","No","Yes","No","Yes"]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)

print("\n")
# Q.2 From the above table that you have created, locate row 0, 4, 7 and 8 using DataFrame. 

selected_rows = df.loc[[0,4,7,8]]
print(selected_rows)

# # Q.3 Navigate the DataFrame and do the following task for the table created in question 1: 
# 1. Select row from index 3 to 7. 
# 2. Select row from index 4 to 8, and column 2 to 4. 
# 3. Select all rows with column index 1 to 3 (include index 3 during selection). 


# Task 1: Select rows from index 3 to 7
rows_3_to_7 = df.loc[3:7]
print("Rows from index 3 to 7:")
print(rows_3_to_7)

print("\n")

# Task 2: Select rows from index 4 to 8 and columns 2 to 4
rows_4_to_8_columns_2_to_4 = df.iloc[4:9, 2:5]
print("Rows from index 4 to 8, Columns 2 to 4:")
print(rows_4_to_8_columns_2_to_4)

print("\n")

# Task 3: Select all rows with column index 1 to 3 (include index 3)
columns_1_to_3 = df.iloc[:, 1:4]
print("All rows with column index 1 to 3:")
print(columns_1_to_3)
