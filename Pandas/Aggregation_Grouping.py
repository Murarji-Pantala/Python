import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York'],
    'Score': [85, 90, 95, 88]
}
df = pd.DataFrame(data)

# Group by City and calculate the mean age and score
grouped_df = df.groupby('City').agg({'Age': 'mean', 'Score': 'mean'})
print("Grouped DataFrame:\n", grouped_df)
