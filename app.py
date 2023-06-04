import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Adatok beolvasása
df = pd.read_csv('adatok2.csv')

# Első öt sor megjelenítése
print(df.head())

# Matplotlib használata egy egyszerű diagramhoz
plt.figure(figsize=(10, 6))
plt.plot(df['YEAR'], df['ESTIMATE'])
plt.title('Matplotlib diagram')
plt.xlabel('YEAR')
plt.ylabel('ESTIMATE')
plt.show()

# Seaborn használata egy bonyolultabb diagramhoz
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x='YEAR', y='ESTIMATE', data=df)
plt.title('Seaborn diagram')
plt.show()

# Hisztogram készítése
plt.figure(figsize=(10, 6))
plt.hist(df['ESTIMATE'], bins=10, edgecolor='black')
plt.title('Histogram of ESTIMATE')
plt.xlabel('ESTIMATE')
plt.ylabel('Frequency')
plt.show()

# Boxplot készítése
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.boxplot(y='ESTIMATE', data=df)
plt.title('Boxplot of ESTIMATE')
plt.show()
