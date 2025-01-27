import pandas as pd

# Create the dataset
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# a) Shape of the DataFrame
print("Shape of the DataFrame:", df.shape)

# b) Summary of the DataFrame
print("\nSummary of the DataFrame:")
print(df.info())

# c) Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# d) Display the first 5 rows and last 3 rows
print("\nFirst 5 Rows:")
print(df.head())
print("\nLast 3 Rows:")
print(df.tail(3))

# e) Calculate statistics
average_salary = df["Salary"].mean()
total_bonus = df["Bonus"].sum()
youngest_age = df["Age"].min()
highest_rating = df["Rating"].max()

print("\nStatistics:")
print(f"Average Salary: {average_salary}")
print(f"Total Bonus: {total_bonus}")
print(f"Youngest Age: {youngest_age}")
print(f"Highest Performance Rating: {highest_rating}")

# f) Sort by Salary in descending order
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nDataFrame sorted by Salary in descending order:")
print(sorted_df)

# g) Add a column categorizing employees based on performance rating
def categorize_rating(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

df["Performance_Category"] = df["Rating"].apply(categorize_rating)
print("\nDataFrame with Performance Category:")
print(df)

# h) Identify missing values
print("\nMissing Values:")
print(df.isnull().sum())

# i) Rename Employee_ID column to ID
df.rename(columns={"Employee_ID": "ID"}, inplace=True)
print("\nDataFrame with Renamed Column:")
print(df)

# j) Find employees with more than 5 years of experience and in IT department
experienced_employees = df[df["Years_of_Experience"] > 5]
it_employees = df[df["Department"] == "IT"]

print("\nEmployees with more than 5 years of experience:")
print(experienced_employees)
print("\nEmployees in IT Department:")
print(it_employees)

# k) Add a new column, Tax, which deducts 10% of the Salary
df["Tax"] = df["Salary"] * 0.1
print("\nDataFrame with Tax Column:")
print(df)

# l) Save the modified DataFrame to a new CSV file
df.to_csv("modified_employees.csv", index=False)
print("\nModified DataFrame saved to 'modified_employees.csv'.")
