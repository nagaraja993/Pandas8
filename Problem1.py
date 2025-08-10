import pandas as pd

# def total_time(employees: pd.DataFrame) -> pd.DataFrame:
#     employees['total_time'] = employees['out_time'] - employees['in_time']
#     print(employees.groupby(["event_day", "emp_id"])['total_time'].transform('sum').reset_index())
#     return employees

# Solution below
def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    return employees.groupby(["event_day", "emp_id"])['total_time']\
                    .agg('sum').reset_index().rename(columns = {'event_day':'day'})
    