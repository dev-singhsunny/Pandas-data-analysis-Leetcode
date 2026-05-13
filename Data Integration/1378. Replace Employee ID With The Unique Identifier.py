import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Merge the DataFrames using the 'id' column and keep only necessary columns
    merged_df = pd.merge(employees, employee_uni, how='left', on='id')
    
    # Select the columns 'unique_id' and 'name' from the merged DataFrame
    result_df = merged_df[['unique_id', 'name']]
    
    return result_df