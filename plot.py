import pandas as pd
import plotly.express as px

# Read your Excel file with xlrd engine
df = pd.read_excel("20nov.xls", engine='xlrd')

# Convert 'Date And Time' to datetime if it's not already
df['Date And Time'] = pd.to_datetime(df['Date And Time'])

# Calculate mean time by date
daily_mean = df.groupby(df['Date And Time'].dt.date)['Date And Time'].mean()

# Create interactive plot with Plotly
fig = px.line(x=daily_mean.index, y=daily_mean.values,
              title='Mean Time Analysis',
              labels={'x': 'Date', 'y': 'Mean Time'},
              markers=True)

# Update layout
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Mean Time",
    # showgrid=True
)

# Save as HTML file (interactive)
fig.write_html("mean_time_analysis.html")
