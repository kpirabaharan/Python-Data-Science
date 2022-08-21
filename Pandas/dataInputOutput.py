import pandas as pd

# CSV
df = pd.read_csv('/home/keeshigan/Documents/DataScience/pandas/example.csv')
# df = pd.read_csv('./example.csv')  # WTF
df

# pd.read_excel('/home/keeshigan/Documents/DataScience/pandas/Excel_Sample.xlsx')

df.to_csv('my_output', index=False)

# Excel
pd.read_excel('/home/keeshigan/Documents/DataScience/pandas/Excel_Sample.xlsx', sheet_name='Sheet1')

df.to_excel('Excel_Sample2.xlsx', sheet_name='NewSheet')

# HTML
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

# Some SQL
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')
df.to_sql('data', engine)
sql_df = pd.read_sql('data', con=engine)
sql_df
