import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
      # 1: Filtra por ids de cliente que não fizeram compra
    # 2: Selecionamos apenas a coluna "name" e renomeamos para Customers sem altera definitvamente o DataFrame.
    return customers[~customers["id"]\
                      .isin(orders["customerId"])][["name"]
                    ]\
        .rename(columns={"name": "Customers"}) 