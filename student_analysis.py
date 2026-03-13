import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("student_data.csv")
# Display first few rows
print("First 5 Records:")
print(df.head())
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Fill missing values with column mean
df = df.fillna(df.mean(numeric_only=True))
# Display basic statistics
print("\nDataset Statistics:")
print(df.describe())
# Subject wise average scores
subject_avg = df[['Math', 'Science', 'English']].mean()
print("\nAverage Scores:")
print(subject_avg)
# Plot subject average scores
subject_avg.plot(kind='bar')
plt.title("Average Score by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()
# Attendance vs Total Score
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
plt.scatter(df['Attendance'], df['Total'])
plt.title("Attendance vs Total Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Total Marks")
plt.show()
