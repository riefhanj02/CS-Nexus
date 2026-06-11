CREATE TABLE `skinitem` (
  `ItemID` int(11) NOT NULL,
  `AssetID` bigint(20) NOT NULL,
  `SkinName` varchar(100) NOT NULL,
  `FloatValue` decimal(18,17) DEFAULT NULL CHECK (`FloatValue` >= 0 and `FloatValue` <= 1.0),
  PRIMARY KEY (`ItemID`),
  UNIQUE KEY `AssetID` (`AssetID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `tradelisting` (
  `ListingID` int(11) NOT NULL,
  `TraderID` int(11) NOT NULL,
  `ItemID` int(11) NOT NULL,
  `AskingPrice` decimal(10,2) NOT NULL,
  PRIMARY KEY (`ListingID`),
  KEY `TraderID` (`TraderID`),
  KEY `ItemID` (`ItemID`),
  CONSTRAINT `tradelisting_ibfk_1` FOREIGN KEY (`TraderID`) REFERENCES `trader` (`TraderID`),
  CONSTRAINT `tradelisting_ibfk_2` FOREIGN KEY (`ItemID`) REFERENCES `skinitem` (`ItemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `trader` (
  `TraderID` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `SteamID64` bigint(20) NOT NULL,
  PRIMARY KEY (`TraderID`),
  UNIQUE KEY `SteamID64` (`SteamID64`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `traderstats` (
  `TraderID` int(11) NOT NULL,
  `TotalTrades` int(11) DEFAULT 0,
  `LastActive` date DEFAULT NULL,
  PRIMARY KEY (`TraderID`),
  CONSTRAINT `traderstats_ibfk_1` FOREIGN KEY (`TraderID`) REFERENCES `trader` (`TraderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `tradetransaction` (
  `TransactionID` int(11) NOT NULL,
  `BuyerID` int(11) NOT NULL,
  `FinalPrice` decimal(10,2) NOT NULL,
  `TimeCompleted` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`TransactionID`),
  KEY `BuyerID` (`BuyerID`),
  CONSTRAINT `tradetransaction_ibfk_1` FOREIGN KEY (`BuyerID`) REFERENCES `trader` (`TraderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `transactionitem` (
  `TransactionID` int(11) NOT NULL,
  `ItemID` int(11) NOT NULL,
  `LinePrice` decimal(10,2) NOT NULL,
  PRIMARY KEY (`TransactionID`,`ItemID`),
  KEY `ItemID` (`ItemID`),
  CONSTRAINT `transactionitem_ibfk_1` FOREIGN KEY (`TransactionID`) REFERENCES `tradetransaction` (`TransactionID`),
  CONSTRAINT `transactionitem_ibfk_2` FOREIGN KEY (`ItemID`) REFERENCES `skinitem` (`ItemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
