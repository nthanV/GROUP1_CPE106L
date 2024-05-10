import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('breadprice.csv', header=0, names=['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index('Year', inplace=True)
avg_price_per_year = df.mean(axis=1)


plt.figure(figsize=(10, 6))
plt.plot(avg_price_per_year.index.year, avg_price_per_year.values)
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.title('Average Price of Bread per Year')
plt.show()