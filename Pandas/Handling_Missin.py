import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, np.nan, 22, 25],
    'City': ['New York', 'Los Angeles', np.nan, 'Houston']
}
df = pd.DataFrame(data)

# Fill missing values with a specified value
df_filled = df.fillna({'Age': df['Age'].mean(), 'City': 'Unknown'})
print("DataFrame with filled missing values:\n", df_filled)

# Drop rows with any missing values
df_dropped = df.dropna()
print("DataFrame with dropped missing values:\n", df_dropped)
