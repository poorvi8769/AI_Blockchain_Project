import pandas as pd

def preprocess_ip_column(df, ip_column):
    """
    Convert IP column to numerical values for model compatibility.
    """
    df[ip_column] = df[ip_column].apply(
        lambda ip: sum(int(octet) for octet in ip.split('.'))
    )
    return df

def load_csv(filepath):
    """
    Load a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(filepath)

def save_csv(df, filepath):
    """
    Save a pandas DataFrame to a CSV file.
    """
    df.to_csv(filepath, index=False)
