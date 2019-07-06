CREATE TABLE `Customers` (
  `CustomersId` int(10) unsigned NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `FirstName` varchar(100) NOT NULL,
  `LastName` varchar(100) NOT NULL,
  `PhoneNo` int(10) NOT NULL,
  `DOB` varchar(100) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `Country` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `City` varchar(100) NOT NULL,
  `PinCode` int(10) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `ProfileImg` varchar(100) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


Category:-

CREATE TABLE `Category` (
  `CategoryId` int(10) unsigned NOT NULL,
  `CategoryName` varchar(255) NOT NULL,
  `Discription` varchar(2000) NOT NULL,
  `Picture` varchar(500) NOT NULL,
  `Active` boolean NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

products:-

CREATE TABLE `Products` (
  `ProductId` int(10) unsigned NOT NULL,
  `SKU` int(100) NOT NULL,
  `ProductName` varchar(100) NOT NULL,
  `ProductDes` varchar(1000) NOT NULL,
  `SupplierId` int(100) NOT NULL,
  `CategoryId` int(100) NOT NULL,
  `QuantityPerUnit` int(100) NOT NULL,
  `UnitPrice` int(50) NOT NULL,
  `MSRP` int(50) NOT NULL,
  `AvilSize` varchar(100) NOT NULL,
  `AvilColor` varchar(100) NOT NULL,
  `Size` int(10) NOT NULL,
  `Colour` varchar(100) NOT NULL,
  `UnitWeight` int(100) NOT NULL,
  `UnitInStock` int(100) NOT NULL,
  `UnitOnOrder` int(100) NOT NULL,
  `ProductAvil` boolean NOT NULL,
  `DiscountAvil` boolean NOT NULL,
  `picture` varchar(500) NOT NULL,
  `Ranking` int(100) NOT NULL,
  `Note` varchar(1000) NOT NULL,
  `Discount` int(100) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



CREATE TABLE `Orders` (
  `OrderId` int(100) unsigned NOT NULL,
  `CustomersId` int(100) NOT NULL,
  `OrderNumber` int(100) NOT NULL,
  `PaymentId` int(100) NOT NULL,
  `OrderDate` varchar(100) NOT NULL,
  `ShipDate` varchar(100) NOT NULL,
  `RequiredDate` varchar(100) NOT NULL,
  `ShipperId` int(100) NOT NULL,
  `Freight` varchar(500) NOT NULL,
  `TimeStamp` varchar(100) NOT NULL,
  `TransactionsStatus` boolean NOT NULL,
  `ErrorMsg` varchar(500) NOT NULL,
  `Fullfilled` varchar(400) NOT NULL,
  `Deleted` boolean NOT NULL,
  `Paid` boolean NOT NULL,
  `PaymentDate` varchar(100) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Payment` (
  `PaymentId` int(10) unsigned NOT NULL,
  `PaymentType` varchar(100) NOT NULL,
  `Allowed` varchar(50) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Shippers` (
  `ShipperId` int(10) unsigned NOT NULL,
  `CompanyName` varchar(100) NOT NULL,
  `PhoneNo` int(10) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `OrderDetails` (
  `OrderId` int(100) unsigned NOT NULL,
  `ProductId` int(100) NOT NULL,
  `OrderNumber` int(100) NOT NULL,
  `Price` int(100) NOT NULL,
  `Qantity` int(100) NOT NULL,
  `Total` int(100) NOT NULL,
  `Discount` int(100) NOT NULL,
  `Size` varchar(100) NOT NULL,
  `Colour` varchar(100) NOT NULL,
  `Fullfilled` varchar(100) NOT NULL,
  `ShipDate` varchar(100) NOT NULL,
  `OrderDetailId` varchar(100) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



CREATE TABLE `Suppliers` (
  `SupplierId` int(100) unsigned NOT NULL,
  `CompanyName` varchar(500) NOT NULL,
  `ContactFirstName` varchar(100) NOT NULL,
  `ContactLastName` varchar(100) NOT NULL,
  `ContactTitle` varchar(100) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `City` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `PinCode` int(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `PhoneNo` int(10) NOT NULL,
  `URL` varchar(100) NOT NULL,
  `PaymentMethod` varchar(100) NOT NULL,
  `DiscountType` varchar(100) NOT NULL,
  `Note` varchar(1000) NOT NULL,
  `CurrentOrder` varchar(500) NOT NULL,
  `Logo` varchar(100) NOT NULL,
  `CustomersId` int(100) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;