import pandas as pd
import hashlib
import os
from datetime import datetime

def analyze_datetime_data(df):
    # Convert the Date And Time column to datetime if not already done
    df['Date And Time'] = pd.to_datetime(df['Date And Time'])
    
    # Define morning hours (e.g., 6 AM to 12 PM)
    morning_data = df[df['Date And Time'].dt.hour.between(6, 12)]
    
    # Analyze busiest morning hour
    morning_hourly_counts = morning_data.groupby(morning_data['Date And Time'].dt.hour).size()
    busiest_morning_hour = morning_hourly_counts.idxmax()
    
    print("\nMorning Hours Analysis (6 AM - 12 PM):")
    print("-" * 40)
    print(f"Busiest morning hour: {busiest_morning_hour}:00")
    print(f"Number of events at that hour: {morning_hourly_counts[busiest_morning_hour]}")
    
    # Show distribution of morning hours
    print("\nMorning hours distribution:")
    print(morning_hourly_counts.sort_values(ascending=False))
    
    # Analyze busiest morning by day of week
    morning_day_counts = morning_data.groupby(morning_data['Date And Time'].dt.day_name()).size()
    busiest_morning_day = morning_day_counts.idxmax()
    
    print("\nBusiest Mornings by Day of Week:")
    print("-" * 40)
    print(f"Busiest morning day: {busiest_morning_day}")
    print(f"Number of morning events: {morning_day_counts[busiest_morning_day]}")
    
    # Show distribution by day of week
    print("\nMorning events by day of week:")
    print(morning_day_counts.sort_values(ascending=False))
    
    # Optional: Add hourly analysis for the busiest day
    busiest_day_data = morning_data[morning_data['Date And Time'].dt.day_name() == busiest_morning_day]
    busiest_day_hours = busiest_day_data.groupby(busiest_day_data['Date And Time'].dt.hour).size()
    
    print(f"\nHourly distribution for {busiest_morning_day} mornings:")
    print(busiest_day_hours.sort_values(ascending=False))


    
    

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
