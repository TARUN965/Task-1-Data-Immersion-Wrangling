import pandas as pd

# Load dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# Check dataset information
print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Feature Engineering
df["Order_Month"] = df["Order_Date"].dt.month_name()
df["Order_Year"] = df["Order_Date"].dt.year

# Create Age Groups
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0,25,35,45,60,100],
    labels=["18-25","26-35","36-45","46-60","60+"]
)

# Save cleaned dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("Task 1 Completed Successfully!")