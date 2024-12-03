import pandas as pd
import hashlib
import os
from datetime import datetime

def analyze_datetime_data(df):
    """
    Analyze the Date And Time column of the DataFrame
    
    Args:
        df (pandas.DataFrame): Input DataFrame containing the date data
    """
    # First convert the Date And Time column to datetime format
    df['Date And Time'] = pd.to_datetime(df['Date And Time'])
    
    # Basic datetime analysis
    print("\nDateTime Analysis:")
    print("-----------------")
    print(f"Earliest date: {df['Date And Time'].min()}")
    print(f"Latest date: {df['Date And Time'].max()}")
    print(f"Date range: {df['Date And Time'].max() - df['Date And Time'].min()}")
    
    # Time-based aggregations
    print("\nData by Month:")
    monthly_counts = df.groupby(df['Date And Time'].dt.month).size()
    print(monthly_counts)
    
    print("\nData by Day of Week:")
    day_of_week_counts = df.groupby(df['Date And Time'].dt.day_name()).size()
    print(day_of_week_counts)
    
    print("\nData by Hour:")
    hourly_counts = df.groupby(df['Date And Time'].dt.hour).size()
    print(hourly_counts)

    # Additional analysis examples you can add to the analyze_datetime_data function:

    # Get average events per day
    daily_counts = df.groupby(df['Date And Time'].dt.date).size()
    print(f"\nAverage events per day: {daily_counts.mean():.2f}")

    # Find busiest day
    busiest_day = daily_counts.idxmax()
    print(f"Busiest day: {busiest_day} with {daily_counts.max()} events")

    # Time differences between consecutive events
    df_sorted = df.sort_values('Date And Time')
    time_differences = df_sorted['Date And Time'].diff()
    print(f"\nAverage time between events: {time_differences.mean()}")


# Modify your main() function to include the analysis
def main():
    # Input file name (your anonymized file)
    input_file = "anonymized_data_20241204_000452.xlsx"
    
    # Read the Excel file
    try:
        df = pd.read_excel(input_file, engine='openpyxl')
        
        # Perform datetime analysis
        analyze_datetime_data(df)
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found!")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()
