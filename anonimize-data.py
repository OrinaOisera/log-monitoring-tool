import pandas as pd
import hashlib
import os
from datetime import datetime

def anonymize_data(df, columns_to_anonymize):
    # Create a copy of the dataframe
    df_anonymized = df.copy()
    
    # Get a secure salt from environment variable or generate one
    salt = os.environ.get('ANONYMIZATION_SALT', os.urandom(16).hex())
    
    def hash_value(value):
        # Convert value to string and combine with salt
        value_to_hash = f"{value}{salt}".encode()
        # Create hash using SHA-256
        return hashlib.sha256(value_to_hash).hexdigest()
    
    # Anonymize specified columns
    for column in columns_to_anonymize:
        if column in df_anonymized.columns:
            df_anonymized[column] = df_anonymized[column].apply(hash_value)
    
    return df_anonymized

# Example usage with your existing code
df = pd.read_excel("page-1.xls", engine='xlrd')

# Specify columns that need to be anonymized
columns_to_anonymize = ['First Name', 'Personnel ID']

# Anonymize the data
df_anonymized = anonymize_data(df, columns_to_anonymize)

# Continue with your visualization code...
