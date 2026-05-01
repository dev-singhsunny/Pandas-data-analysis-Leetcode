import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['category']=pd.cut(accounts['income'], 
    bins=[-float('inf'), 19999, 50000, float('inf')],
    labels=['Low Salary', 'Average Salary', 'High Salary'])
    count= accounts['category'].value_counts().reset_index()
    count.columns=['category','accounts_count']
    return count