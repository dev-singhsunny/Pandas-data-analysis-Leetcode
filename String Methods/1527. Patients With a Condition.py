import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
       return patients[
        patients["conditions"].apply(
            lambda x: any(i.startswith("DIAB1") for i in x.split())
        )
    ]    