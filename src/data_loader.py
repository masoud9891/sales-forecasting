import pandas as pd


def load_sales_data(path='../data/sales_data.csv'):
    """
    Load sales data from a CSV file.

    Args:
        path (str): The file path to the sales data CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the sales data.
    """
    df = pd.read_csv(path)
    return df