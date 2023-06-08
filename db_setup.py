import settings
import sqlite3
import pandas as pd
con = sqlite3.connect(settings.SQLITE_DB_PATH)

with open(settings.SQLITE_DB_SQL, mode='r') as f:
    con.cursor().executescript(f.read())

print("Table created successfully")

print("Start import data")

df = pd.read_csv(settings.BILL_CSV_PATH)

df = df[['bill/PayerAccountId', 'lineItem/UnblendedCost', 'lineItem/UnblendedRate', 'lineItem/UsageAccountId', 'lineItem/UsageAmount',
        'lineItem/UsageStartDate', 'lineItem/UsageEndDate', 'product/ProductName']]

df.to_sql('billings', con=con, index=False, if_exists='replace')

con.close()
print("Data imported")
