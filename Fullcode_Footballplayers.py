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



#6


# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the Manchester City players data
df_mancity = pd.read_csv('dataset/manchester_city_player_stats.csv')

# Step 1: Handle missing values
# Fill missing numerical values with 0 (assuming missing means no activity)
df_mancity.fillna({'Apearances': 0, 'Substitutions': 0, 'Goals': 0, 'Penalties': 0, 'YellowCards': 0, 'RedCards': 0}, inplace=True)

# Step 2: Encode categorical variables (Position)
label_encoder = LabelEncoder()
df_mancity['Position_Encoded'] = label_encoder.fit_transform(df_mancity['Position'])

# Step 3: Create a new feature (Goals per Appearance)
df_mancity['Goals_per_Appearance'] = df_mancity['Goals'] / df_mancity['Apearances'].replace(0, 1)  # Avoid division by zero

# Step 4: Display the updated dataframe
print("✅ Updated DataFrame with encoded Position and new feature:")
print(df_mancity[['Player', 'Position', 'Position_Encoded', 'Goals', 'Apearances', 'Goals_per_Appearance']].head())

# Step 5: Correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(df_mancity[['Apearances', 'Goals', 'Penalties', 'YellowCards', 'RedCards', 'Goals_per_Appearance']].corr(), 
            annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Numerical Features', fontsize=14)
plt.show()



#7


import pandas as pd

# Load match results
df_matches = pd.read_csv('dataset/all_match_results.csv')   

# Standardize team name to match exactly
df_matches['HomeTeam'] = df_matches['HomeTeam'].str.strip()
df_matches['AwayTeam'] = df_matches['AwayTeam'].str.strip()

# Filter matches involving Manchester City
df_mc_matches = df_matches[
    (df_matches['HomeTeam'] == 'Manchester City') |
    (df_matches['AwayTeam'] == 'Manchester City')
].copy()

# Convert date to datetime format
df_mc_matches['Date'] = pd.to_datetime(df_mc_matches['Date'], format='%d-%b-%Y')

# Sort by date
df_mc_matches.sort_values('Date', inplace=True)

# نمایش چند سطر اول
print(df_mc_matches.head())


import pandas as pd

# فرض کن دیتافریم اصلی بازی‌هاست
df_matches = pd.read_csv('dataset/all_match_results.csv')  # یا هر فایل خودت

# تبدیل ستون Date به datetime و استخراج year و month
df_matches['Date'] = pd.to_datetime(df_matches['Date'])
df_matches['year'] = df_matches['Date'].dt.year
df_matches['month'] = df_matches['Date'].dt.month

# فیلتر بازی‌های منچستر سیتی (خانگی یا مهمان)
df_mc_matches = df_matches[(df_matches['HomeTeam'] == 'Manchester City') | (df_matches['AwayTeam'] == 'Manchester City')].copy()

# ذخیره به فایل جدید csv
df_mc_matches.to_csv('dataset/manchester_city_matches.csv', index=False)

# نمایش چند ردیف اول
print(df_mc_matches.head())


import pandas as pd

# بارگذاری دیتاست آب‌وهوا
weather_df = pd.read_csv('dataset/MET Office Weather Data.csv')

# نمایش ستون‌ها و 5 سطر اول برای بررسی اولیه
print("ستون‌ها:")
print(weather_df.columns)
print("\n۵ سطر اول:")
print(weather_df.head())

# نمایش مقادیر یکتای ستون ایستگاه (station)
print("\nایستگاه‌های موجود در ستون 'station':")
print(weather_df['station'].unique())

# فیلتر کردن داده‌های مربوط به منچستر یا ringway
manchester_weather_df = weather_df[
    weather_df['station'].str.contains('manchester|ringway', case=False, na=False)
].copy()

# نمایش چند سطر اول از داده‌های منچستر
print("\n۵ سطر اول از داده‌های منچستر یا Ringway:")
print(manchester_weather_df.head())



close_stations = ['shawbury', 'bradford', 'sheffield']
recent_weather = weather_df[weather_df['year'].isin([2019, 2020])]
valid_stations = recent_weather[recent_weather['station'].isin(close_stations)]['station'].unique()

print("ایستگاه‌های نزدیک با دیتای ۲۰۱۹ و ۲۰۲۰:", valid_stations)


# فیلتر کردن داده‌ها
filtered_weather = weather_df[
    (weather_df['year'].isin([2019, 2020])) &
    (weather_df['station'].isin(['bradford', 'shawbury', 'sheffield']))
].copy()

# فقط ستون‌های عددی (year, month, tmax, tmin, af, rain, sun)
numeric_cols = ['year', 'month', 'tmax', 'tmin', 'af', 'rain', 'sun']

# میانگین‌گیری برای هر سال و ماه
monthly_avg_weather = filtered_weather[numeric_cols].groupby(['year', 'month']).mean().reset_index()

print(monthly_avg_weather.head())


# فرض کنیم داده‌های آب و هوا فقط برای ۲۰۱۸ و ۲۰۱۹ داریم
available_years = monthly_avg_weather['year'].unique()

# تعریف year_for_weather با یک سال عقب تر
df_mc_matches['year_for_weather'] = df_mc_matches['year'] - 1

# اگر year_for_weather توی داده‌های آب و هوا نیست، اون رو به نزدیک‌ترین سال موجود تغییر میدیم
df_mc_matches['year_for_weather'] = df_mc_matches['year_for_weather'].apply(
    lambda y: max(y for y in available_years if y <= y)
)

# اطمینان از نوع صحیح ستون‌ها برای merge
df_mc_matches['year_for_weather'] = df_mc_matches['year_for_weather'].astype(int)
df_mc_matches['month'] = df_mc_matches['month'].astype(int)
monthly_avg_weather['year'] = monthly_avg_weather['year'].astype(int)
monthly_avg_weather['month'] = monthly_avg_weather['month'].astype(int)

# مرج کردن دیتا
merged_df = df_mc_matches.merge(monthly_avg_weather, left_on=['year_for_weather', 'month'], right_on=['year', 'month'], how='left')


df_weather = pd.read_csv("dataset/MET Office Weather Data.csv")
print(df_weather.shape)
print(df_weather.head())


import pandas as pd

# ایستگاه‌های انتخاب‌شده
stations_of_interest = ['bradford', 'shawbury', 'sheffield']

# فیلتر فقط سال‌های ۲۰۱۹ و ۲۰۲۰
filtered_weather = weather_df[
    (weather_df['year'].isin([2019, 2020])) &
    (weather_df['station'].isin(stations_of_interest))
].copy()

# میانگین‌گیری ماهانه
monthly_avg_weather = (
    filtered_weather
    .groupby(['year', 'month'], as_index=False)
    .mean(numeric_only=True)
)

# افزودن ستون station به عنوان "avg_manchester"
monthly_avg_weather['station'] = 'avg_manchester'

# افزودن به دیتافریم اصلی
weather_df = pd.concat([weather_df, monthly_avg_weather], ignore_index=True)
weather_dfimport pandas as pd

# فرض بر این‌که weather_df شامل avg_manchester است:
# ['year', 'month', 'tmax', 'tmin', 'af', 'rain', 'sun', 'station']

# 1. فیلتر روی avg_manchester
avg_weather = weather_df[weather_df['station'] == 'avg_manchester'].copy()

# 2. میانگین‌گیری فقط بر اساس ماه (بدون سال)
monthly_weather = (
    avg_weather
    .groupby('month', as_index=False)
    .agg({
        'tmax': 'mean',
        'tmin': 'mean',
        'af':  'mean',
        'rain':'mean',
        'sun': 'mean'
    })
)

# 3. نمایش DataFrame نهایی هواشناسی بر اساس ماه
print(monthly_weather)



merged_df = df_matches.merge(monthly_weather, on='month', how='left')
print(merged_df[['Date', 'HomeTeam', 'AwayTeam', 'month', 'tmax', 'tmin', 'rain', 'sun']].head())


df_merged.to_csv('dataset/matches_with_weather.csv', index=False)

