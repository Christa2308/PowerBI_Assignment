import pandas as pd
 
 
df = pd.read_csv("C:/Users/Julienne Ayinkamiye/Downloads/archive/uber.csv")

 
print("First 5 rows of the dataset:")
print(df.head())

 
print("\nDataset Info:")
print(df.info())

 
print("\nColumns in dataset:")
print(df.columns.tolist())

 
print("\nMissing values per column:")
print(df.isnull().sum())
 
df_clean = df.dropna()
 
df_clean['pickup_datetime'] = pd.to_datetime(df_clean['pickup_datetime'])
 
df_clean = df_clean.drop_duplicates()


 
print("\nData shape after cleaning:", df_clean.shape)
 
print("\nData types after cleanup:")
print(df_clean.dtypes)

 
df_clean['hour'] = df_clean['pickup_datetime'].dt.hour
df_clean['day'] = df_clean['pickup_datetime'].dt.day
df_clean['month'] = df_clean['pickup_datetime'].dt.month
df_clean['day_of_week'] = df_clean['pickup_datetime'].dt.dayofweek
df 
def classify_peak(hour):
    return "Peak" if (7 <= hour <= 9 or 16 <= hour <= 19) else "Off-Peak"

df_clean['peak_time'] = df_clean['hour'].apply(classify_peak)
 
print("\n Data types after feature engineering:")
print(df_clean.dtypes)

df_clean.to_csv(r"C:\Users\Julienne Ayinkamiye\Documents\enhanced_uber_fares.csv", index=False)

df_encoded = pd.get_dummies(df_clean, columns=['day_of_week', 'month', 'peak_time'], drop_first=False)

encoded_columns_only = df_encoded.filter(regex='day_of_week_|month_|peak_time_')
print(encoded_columns_only.head())
 
 
print("\n Encoded columns preview:")
print(df_encoded.columns.tolist())

print("\n  First few rows of encoded dataset:")
print(df_encoded.head())
 
df_encoded.to_csv(r"C:\Users\Julienne Ayinkamiye\Documents\enhanced_encoded_uber_fares.csv", index=False)
print(" Enhanced and encoded dataset saved for Power BI.")

import matplotlib.pyplot as plt
import seaborn as sns

print("\nDescriptive Statistics:")
print(df_clean.describe())
 
plt.figure(figsize=(8, 5))
sns.histplot(df_clean['fare_amount'], bins=50, kde=True)
plt.title("Fare Amount Distribution")
plt.xlabel("Fare ($)")
plt.ylabel("Frequency")
plt.show()
 
df_clean['hour'] = df_clean['pickup_datetime'].dt.hour
 
plt.figure(figsize=(10, 5))
sns.boxplot(x='hour', y='fare_amount', data=df_clean)
plt.title("Fare Amount by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Fare Amount")
plt.show()

   

 

  
