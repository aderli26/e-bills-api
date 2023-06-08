
DROP TABLE IF EXISTS `billings`;

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

CREATE INDEX `product/ProductName_index` on `billings` (`product/ProductName`);
CREATE INDEX `lineItem/UsageAccountId_index` on `billings` (`lineItem/UsageAccountId`);
