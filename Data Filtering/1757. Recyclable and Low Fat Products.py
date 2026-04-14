import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    new_df = pd.DataFrame()
    new_df = products[ (products["low_fats"] == 'Y') & (products["recyclable"] == 'Y')]
    new_df.drop(columns=["recyclable","low_fats"], inplace=True)
    return new_df