import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (employees['employee_id']%2==1) & (~(employees['name'].str[0] ==('M')))
    employees.salary*= mask
    return employees.rename(columns={'salary': 'bonus'}).sort_values(by='employee_id').iloc[:,[0, 2]]