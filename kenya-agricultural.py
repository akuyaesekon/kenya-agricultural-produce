import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("C:/Users/Admin/OneDrive/Desktop/kenya-agricultural-produce/Kenya_Agricultural_Production.xlsx")

df

df.shape

df.info

df.dtypes

df.head(10)

# Saving the first 10 rows to a CSV file
data = df.head(10)
data.to_csv("first_10_rows.csv", index=False)

# Saving the first 10 rows to an Excel file
data.to_excel("first_10_rows.xlsx", index=False)

data

data.drop_duplicates

data

data.fillna
data

data.columns

# Count occurrences of different domains
domain_count = df['Domain'].value_counts()

# Bar chart showing the count of production in each domain
domain_count.plot(kind='bar')
plt.title('Count of Production per Domain')
plt.xlabel('Domain')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# Count occurrences for each area (e.g., 'Kenya')
area_count = df['Area'].value_counts()

# Bar chart showing production per area
area_count.plot(kind='bar')
plt.title('Production by Area')
plt.xlabel('Area')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# Count occurrences for each element
element_count = df['Element'].value_counts()

# Bar chart for element distribution
element_count.plot(kind='bar')
plt.title('Distribution of Elements')
plt.xlabel('Element')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# Filter for a specific item (e.g., 'Abaca, manila hemp, raw')
item_data = df[df['Item'] == 'Abaca, manila hemp, raw']

# Bar chart of production by year for the selected item
plt.bar(item_data['Year'], item_data['Value'])
plt.title('Production of Abaca (Manila Hemp) Over the Years')
plt.xlabel('Year')
plt.ylabel('Production (tonnes)')
plt.show()

# Plot production over the years for all items
df.groupby('Year')['Value'].sum().plot(kind='line')
plt.title('Total Agricultural Production Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Production (tonnes)')
plt.show()

