import sqlite3
from flask import Flask,request
import pandas as pd
import settings

def connect_db():
    con = sqlite3.connect(settings.SQLITE_DB_PATH)
    return con

app = Flask(__name__)


@app.route('/api/unblendedcost',methods = ['GET'])
def unblendedcost():
    usage_accountid=request.args.get('usageaccountid')
    if not usage_accountid:
        return "missing usageaccountid parameter"
    con = connect_db()
    query=f'''SELECT `product/ProductName`,`lineItem/UnblendedCost` FROM billings where 
    `lineItem/UsageAccountId` = "{usage_accountid}"'''
    df=pd.read_sql(query,con)
    con.close()


    # group by product/ProductName to sum UnblendedCost
    df=df.groupby('product/ProductName')['lineItem/UnblendedCost'].sum().round(4)

    return df.astype(str).to_dict()

@app.route('/api/usageamount',methods = ['GET'])
def usageamount():
    usage_accountid=request.args.get('usageaccountid')
    if not usage_accountid:
        return "missing usageaccountid parameter"
    con = connect_db()
    query=f'''SELECT `product/ProductName`,`lineItem/UsageAmount`,STRFTIME('%Y-%m-%d',`lineItem/UsageEndDate`) date
    FROM billings where 
    `lineItem/UsageAccountId` = "{usage_accountid}"'''
    df=pd.read_sql(query,con)
    con.close()
    
    # group by product/ProductName and date to sum UsageAmount
    df=df.groupby(['product/ProductName','date'])['lineItem/UsageAmount'].sum().round(4)
    result_dict=df.astype(str).to_dict()
    output_dict = {}
    for key, value in result_dict.items():
        name, date = key
        if name not in output_dict:
            output_dict[name] = {}
        output_dict[name][date] = value

    return output_dict

if __name__ == '__main__':
    app.run(debug=True)

