import pandas as pd

# Read data from a CSV file
df = pd.read_csv('data.csv')
print("Data read from CSV file:\n", df)

# Write the DataFrame to a new CSV file
df.to_csv('new_data.csv', index=False)
print("Data written to new_data.csv")
