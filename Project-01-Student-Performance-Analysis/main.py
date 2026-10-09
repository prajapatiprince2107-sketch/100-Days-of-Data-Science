print("Welcome to Stundent Performance Analysis!")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("All libraies imported successfully!")

data = {
    "Student": ["Amit", "Priya", "Rahul", "Neha", "Jay"],
    "Maths": [85, 92, 67, 78, 88],
    "Science": [90, 95, 72, 80, 85],
    "English": [78, 88, 75, 85, 82]
}
df = pd.DataFrame(data)

print("\nStudnet Dataset:")
print(df)

# Calculate average marks of each student
df["Average"] = df[["Maths","Science","English"]].mean(axis=1)

print("\nStudent average Marks:")
print(df[["Student","Average"]])

#Find the highest scorer
top_student = df.loc[df["Average"].idxmax()]

print("\nTop performing Student:")
print(top_student[["Student","Average"]])

# Subject-wise Average Marks

subjects = ["Maths", "Science", "English"]

average_marks = [
    df["Maths"].mean(),
    df["Science"].mean(),
    df["English"].mean()
]

plt.figure(figsize=(8,5))

sns.barplot(x=subjects, y=average_marks)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.tight_layout()
plt.show()