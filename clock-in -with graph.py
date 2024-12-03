import pandas as pd
import matplotlib.pyplot as plt

# Read your Excel file with xlrd engine
df = pd.read_excel("20nov.xls", engine='xlrd')

# Convert 'Date And Time' to datetime if it's not already
df['Date And Time'] = pd.to_datetime(df['Date And Time'])

# Calculate mean time by date
# This groups by date and calculates the mean time
daily_mean = df.groupby(df['Date And Time'].dt.date)['Date And Time'].mean()

# Create the plot
plt.figure(figsize=(10, 6))
daily_mean.plot(kind='line', marker='o')

# Customize the plot
plt.title('Mean Time Analysis')
plt.xlabel('Date')
plt.ylabel('Mean Time')
plt.grid(True)
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot
plt.savefig('mean_time_analysis.png')
plt.show()
