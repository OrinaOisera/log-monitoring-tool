import pandas as pd
import hashlib
import os
from datetime import datetime

def anonymize_data(df, columns_to_anonymize):
    """
    Anonymize specified columns in a pandas DataFrame using SHA-256 hashing.
    
    Args:
        df (pandas.DataFrame): Input DataFrame containing data to anonymize
        columns_to_anonymize (list): List of column names to anonymize
    
    Returns:
        pandas.DataFrame: Copy of input DataFrame with specified columns anonymized
    """
    # Create a copy of the dataframe
    df_anonymized = df.copy()
    
    # Get a secure salt from environment variable or generate one
    salt = os.environ.get('ANONYMIZATION_SALT', os.urandom(16).hex())
    
    def hash_value(value):
        """Hash a value using SHA-256 with salt."""
        # Convert value to string and combine with salt
        value_to_hash = f"{value}{salt}".encode()
        # Create hash using SHA-256
        return hashlib.sha256(value_to_hash).hexdigest()
    
    # Anonymize specified columns
    for column in columns_to_anonymize:
        if column in df_anonymized.columns:
            df_anonymized[column] = df_anonymized[column].apply(hash_value)
            
    return df_anonymized

def main():
    # Input and output file names
    input_file = "page-1.xls"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"anonymized_data_{timestamp}.xlsx"  # Changed to .xlsx
    
    # Read the Excel file
    try:
        df = pd.read_excel(input_file, engine='xlrd')
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found!")
        return
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return
    
    # Specify columns that need to be anonymized
    columns_to_anonymize = ['First Name', 'Personnel ID']
    
    # Anonymize the data
    df_anonymized = anonymize_data(df, columns_to_anonymize)
    
    # Save the anonymized data to a new Excel file
    try:
        df_anonymized.to_excel(output_file, index=False, engine='openpyxl')
        print(f"Successfully saved anonymized data to '{output_file}'")
    except Exception as e:
        print(f"Error saving file: {str(e)}")

if __name__ == "__main__":
    main()