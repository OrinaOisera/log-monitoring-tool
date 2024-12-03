import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, date

# Read your Excel file with xlrd engine
df = pd.read_excel("20nov.xls", engine='xlrd')

# Convert 'Date And Time' to datetime if it's not already
df['Date And Time'] = pd.to_datetime(df['Date And Time'])

# Create a reference date (today's date) to combine with time for y-axis
ref_date = date.today()

# Convert times to datetime using the reference date
y_axis_times = [datetime.combine(ref_date, t) for t in df['Date And Time'].dt.time]

# Create the plot
plt.figure(figsize=(12, 6))
plt.scatter(df['Date And Time'], y_axis_times, 
           color='#2E86C1', 
           alpha=0.6,
           s=100)  # Size of points

# Customize the plot
plt.title('Check-in Times Progression', fontsize=14, pad=20)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Time of Day', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Format y-axis to show only time
plt.gca().yaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gcf().autofmt_xdate()  # Better date format on x-axis

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot
plt.savefig('checkin_progression.png', dpi=300, bbox_inches='tight')
plt.show()
