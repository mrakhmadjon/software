
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('covid_19_clean.csv')

# Filter the data for Poland
poland_data = data[data['Country/Region'] == 'Poland']

# Convert the 'Date' column to datetime
poland_data['Date'] = pd.to_datetime(poland_data['Date'])

# Plot the number of recovered individuals versus date
plt.figure(figsize=(10, 6))
plt.plot(poland_data['Date'], poland_data['Recovered'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Number of Recovered Individuals')
plt.title('Number of Recovered Individuals in Poland Over Time')
plt.xticks(rotation=45)  # Rotate the date labels for better visibility
plt.tight_layout()  # Adjust layout to make room for rotated labels
plt.show()

# Find and print the earliest date with positive recovered cases
positive_recovered = poland_data[poland_data['Recovered'] > 0]
earliest_positive_date = positive_recovered['Date'].min()
print(f"The earliest date when the number of recovered individuals in Poland is positive: {earliest_positive_date.date()}")



#######################3

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('covid_19_clean.csv')

# Filter the data for Poland
data = df[((df["Country/Region"] == "Poland") & (df['Recovered']))]

first_day = df[((df["Country/Region"] == "Poland") & (df['Recovered'] > 0))]

print(first_day)

number = list(data["Recovered"])
print(number)

numeric_data = []

plt.xticks(range(0,100,15))

plt.plot(number)

plt.title("Poland")

plt.show()

