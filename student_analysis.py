import pandas as pd

# Q.1. Read CSV
df = pd.read_csv("students.csv")

print("Full Student DataSet :")
print(df)

# Q.2. Students age > 10
age_above_10 = df[df["Age"] > 10]
print("\nStudents Age Above 10 :")
print(age_above_10)

# Q.3. Students in Grade 5th
grade_5 = df[df["Grade"] == 5]
print("\nStudents in Grade 5th :")
print(grade_5)

# Q.4. Average age
avg_age = df["Age"].mean()
print("\nStudent Average Age:", avg_age)

# Q.5. Students age above average
above_avg = df[df["Age"] > avg_age]
print("\nStudents Above Average Age :")
print(above_avg)