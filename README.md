# Assignment - API Enhancement
## API URL & SPEC


---
###  Get __lineItem/UnblendedCost__ grouping by __product/productname__


### Request
| Method | URL  | 
|-------|:-----:|
| GET   |  http://127.0.0.1:5000/api/unblendedcost |

### Path parameter 
| Name | Data type  |Required| Example |
|-------|:-----:|:-----:|:-----:|
| usageaccountid |String  |True| 610810069647 |
### Response body example
```json
{
    "AWS CloudTrail": "0.0",
    "AWS Cost Explorer": "9.87",
    "AWS Key Management Service": "0.0",
    "AWS Premium Support": "4569.04",
    "Amazon DynamoDB": "0.0",
    "Amazon Elastic Compute Cloud": "8914.1195",
    "Amazon Simple Storage Service": "2.6955",
    "AmazonCloudWatch": "0.0",
    "Savings Plans for AWS Compute usage": "0.0"
}
```
---
###  Get __lineItem/UnblendedCost__ grouping by __product/productname__


### Request
| Method | URL  | 
|-------|:-----:|
| GET   |  http://127.0.0.1:5000/api/usageamount |

### Path parameter 
| Name | Data type  |Required| Example |
|-------|:-----:|:-----:|:-----:|
| usageaccountid |String  |True| 610810069647 |
### Response body example
```json
{
  "AWS CloudTrail": {
    "2020-04-01": "396.0",
    "2020-04-02": "455.0",
    "2020-04-03": "243.0",
    "2020-04-04": "701.0",
    "2020-04-05": "261.0",
    "2020-04-06": "217.0",
    "2020-04-07": "1109.0",
    "2020-04-09": "1441.0",
    "2020-04-10": "777.0",
    "2020-04-12": "882.0",
    "2020-04-14": "874.0",
    "2020-04-15": "1461.0",
    "2020-04-16": "399.0",
    "2020-04-17": "1831.0",
    "2020-04-18": "131.0",
    "2020-04-19": "266.0",
    "2020-04-20": "163.0",
    "2020-04-21": "1828.0",
    "2020-04-22": "666.0",
    "2020-04-23": "90.0",
    "2020-04-24": "455.0",
    "2020-04-25": "315.0",
    "2020-04-26": "75.0",
    "2020-04-27": "153.0",
    "2020-04-28": "807.0",
    "2020-04-29": "299.0",
    "2020-04-30": "15.0",
    "2020-05-01": "194.0"
  },
  ...
}
```
---
## DB schema
### SQLite bills.db
```
CREATE TABLE `billings`(
  `bill/PayerAccountId` INT NOT NULL,
  `lineItem/UnblendedCost` FLOAT NULL,
  `lineItem/UnblendedRate` FLOAT NULL,
  `lineItem/UsageAccountId` INT NULL,
  `lineItem/UsageAmount` FLOAT NULL,
  `lineItem/UsageStartDate` DATETIME NULL,
  `lineItem/UsageEndDate` DATETIME NULL,
  `product/ProductName` VARCHAR(255) NULL,
  PRIMARY KEY (`bill/PayerAccountId`));

CREATE INDEX `product/ProductName_index` on `billings`
(`product/ProductName`);
CREATE INDEX `lineItem/UsageAccountId_index` on `billings` 
(`lineItem/UsageAccountId`);
```

## Steps
### 1.Install packages
```
pip install -r requirements.txt
```
### 2.Initialize DB
```
python db_setup.py
```
### 3.Start server
```
python app.py
```