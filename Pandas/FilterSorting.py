import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Filter rows where Age is greater than 24
filtered_df = df[df['Age'] > 24]
print("Filtered DataFrame:\n", filtered_df)

# Sort the DataFrame by Age
sorted_df = df.sort_values(by='Age')
print("Sorted DataFrame:\n", sorted_df)
