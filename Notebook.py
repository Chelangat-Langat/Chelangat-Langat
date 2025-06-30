import pandas as pd

def handle_missing_values(df, strategy='mean', drop_threshold=0.5):
    """
    Handle missing values in a DataFrame by filling or dropping columns.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - strategy (str): Strategy to fill missing values: 'mean', 'median', or 'mode'.
    - drop_threshold (float): If more than this fraction of a column is missing, drop the column.

    Returns:
    - pd.DataFrame: Cleaned DataFrame.
    """
    df_cleaned = df.copy()

    # Drop columns with too many missing values
    missing_fraction = df_cleaned.isnull().mean()
    cols_to_drop = missing_fraction[missing_fraction > drop_threshold].index
    df_cleaned.drop(columns=cols_to_drop, inplace=True)

    # Fill remaining missing values
    for col in df_cleaned.columns:
        if df_cleaned[col].isnull().any():
            if strategy == 'mean' and df_cleaned[col].dtype in ['float64', 'int64']:
                df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)
            elif strategy == 'median' and df_cleaned[col].dtype in ['float64', 'int64']:
                df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)
            else:
                df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)

    return df_cleaned
