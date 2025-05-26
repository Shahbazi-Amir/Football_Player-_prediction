import pandas as pd

# لود فایل اصلی بازیکنان
df_players = pd.read_csv('all_players_stats.csv')

# فیلتر بازیکنان منچستر سیتی
df_mancity = df_players[df_players['Team'] == 'Manchester City']

# نمایش ستون‌های مهم (اصلاح شده)
print("✅ بازیکنان منچستر سیتی:")
print(df_mancity[['Player', 'Position', 'Apearances', 'Goals', 'Penalties']].head())

# ذخیره در فایل جدید
df_mancity.to_csv('manchester_city_player_stats.csv', index=False)



#2
# خلاصه آماری ستون‌های عددی
print("📊 خلاصه آماری ستون‌های عددی:")
print(df_mancity[['Apearances', 'Goals', 'Penalties']].describe())



#3
import matplotlib.pyplot as plt
import seaborn as sns

# تنظیم استایل برای زیبایی بیشتر
sns.set(style="whitegrid")

# رسم هیستوگرام تعداد گل‌ها
plt.figure(figsize=(10, 6))
sns.histplot(data=df_mancity, x='Goals', bins=10, kde=True, color='skyblue')
plt.title('Distribution of Goals Scored by Manchester City Players', fontsize=14)
plt.xlabel('Number of Goals')
plt.ylabel('Number of Players')
plt.show()




#4
plt.figure(figsize=(10, 6))
sns.barplot(data=df_mancity, x='Position', y='Goals', hue='Position', palette='viridis', estimator='mean', legend=False)
plt.title('Average Goals by Position', fontsize=14)
plt.xlabel('Player Position')
plt.ylabel('Average Number of Goals')
plt.xticks(rotation=15)
plt.show()




#5
import pandas as pd

# Load the Manchester City players data
df_mancity = pd.read_csv('manchester_city_player_stats.csv')

# Show first 5 rows to inspect data
print("First 5 rows of the data:")
print(df_mancity.head())

# Check for missing values in each column
print("\nMissing values per column:")
print(df_mancity.isnull().sum())

# Show data types of each column
print("\nData types of each column:")
print(df_mancity.dtypes)

# Get descriptive statistics of numerical columns
print("\nDescriptive statistics of numerical columns:")
print(df_mancity.describe())
