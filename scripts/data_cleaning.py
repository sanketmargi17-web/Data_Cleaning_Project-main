import pandas as pd

print("Script Started")

# Load dataset
df = pd.read_csv("../raw_data/Superstore.csv", encoding='latin1')

# Show first rows
print(df.head())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df = df.fillna({
    'Sales': 0,
    'Profit': 0
})

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create Year column
df['Year'] = df['Order Date'].dt.year

# Create Month column
df['Month'] = df['Order Date'].dt.month_name()

# Save cleaned file
df.to_csv("../cleaned_data/cleaned_sales_data.csv", index=False)

print("Data Cleaning Completed Successfully!")