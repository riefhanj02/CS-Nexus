import streamlit as st
import mysql.connector
import pandas as pd
import json
import os

# Set up page configurations
st.set_page_config(page_title="CS-Nexus Hybrid Data System", layout="wide", page_icon="🎮")

# ==========================================================================
# Database Connection Configs & Helper Functions
# ==========================================================================

st.sidebar.title("🔌 Database Settings")
db_host = st.sidebar.text_input("MySQL Host", value="127.0.0.1")
db_user = st.sidebar.text_input("Username", value="root")
db_pass = st.sidebar.text_input("Password", value="", type="password")
db_name = st.sidebar.text_input("Database Name", value="cs_nexus")

def get_db_connection():
    """Establish connection to local MySQL database."""
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_pass,
        database=db_name,
        connect_timeout=3
    )

# Load semi-structured data
def load_json_data():
    """Load sticker configuration metadata from JSON file."""
    json_path = "data_store/skin_stickers.json"
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# ==========================================================================
# Mock Data Store (Offline Failover Mode)
# ==========================================================================

MOCK_LISTINGS = [
    {
        'AskingPrice': 150.0,
        'AssetID': 9988776655,
        'FloatValue': 0.04501234567890123,
        'ItemID': 101,
        'ListingID': 1001,
        'SkinName': 'AK-47 | Vulcan (Factory New)',
        'Username': 'car'
    },
    {
        'AskingPrice': 25.5,
        'AssetID': 9988776663,
        'FloatValue': 0.22,
        'ItemID': 109,
        'ListingID': 1002,
        'SkinName': 'AK-47 | Redline (Field-Tested)',
        'Username': 'car'
    },
    {
        'AskingPrice': 85.0,
        'AssetID': 9988776664,
        'FloatValue': 0.28,
        'ItemID': 110,
        'ListingID': 1003,
        'SkinName': 'AWP | Asiimov (Field-Tested)',
        'Username': 'car'
    },
    {
        'AskingPrice': 2400.0,
        'AssetID': 9988776658,
        'FloatValue': 0.11055555555555555,
        'ItemID': 104,
        'ListingID': 1019,
        'SkinName': 'M4A4 | Howl (Minimal Wear)',
        'Username': 'car'
    },
    {
        'AskingPrice': 2150.0,
        'AssetID': 9988776662,
        'FloatValue': 0.03,
        'ItemID': 108,
        'ListingID': 1023,
        'SkinName': 'Butterfly Knife | Fade (Factory New)',
        'Username': 'car'
    },
    {
        'AskingPrice': 3500.0,
        'AssetID': 9988776656,
        'FloatValue': 0.2501234567890123,
        'ItemID': 102,
        'ListingID': 1004,
        'SkinName': 'AWP | Dragon Lore (Field-Tested)',
        'Username': 'potsu_420'
    },
    {
        'AskingPrice': 1200.0,
        'AssetID': 9988776657,
        'FloatValue': 0.01599999999999999,
        'ItemID': 103,
        'ListingID': 1005,
        'SkinName': 'Karambit | Doppler (Factory New)',
        'Username': 'potsu_420'
    },
    {
        'AskingPrice': 2100.0,
        'AssetID': 9988776662,
        'FloatValue': 0.03,
        'ItemID': 108,
        'ListingID': 1006,
        'SkinName': 'Butterfly Knife | Fade (Factory New)',
        'Username': 'potsu_420'
    },
    {
        'AskingPrice': 310.0,
        'AssetID': 9988776659,
        'FloatValue': 0.02011111111111111,
        'ItemID': 105,
        'ListingID': 1020,
        'SkinName': 'Desert Eagle | Blaze (Factory New)',
        'Username': 'potsu_420'
    },
    {
        'AskingPrice': 26.0,
        'AssetID': 9988776663,
        'FloatValue': 0.22,
        'ItemID': 109,
        'ListingID': 1024,
        'SkinName': 'AK-47 | Redline (Field-Tested)',
        'Username': 'potsu_420'
    },
    {
        'AskingPrice': 45.0,
        'AssetID': 9988776661,
        'FloatValue': 0.85,
        'ItemID': 107,
        'ListingID': 1007,
        'SkinName': 'USP-S | Kill Confirmed (Battle-Scarred)',
        'Username': 'JYniuBi'
    },
    {
        'AskingPrice': 24.0,
        'AssetID': 9988776663,
        'FloatValue': 0.22,
        'ItemID': 109,
        'ListingID': 1008,
        'SkinName': 'AK-47 | Redline (Field-Tested)',
        'Username': 'JYniuBi'
    },
    {
        'AskingPrice': 80.0,
        'AssetID': 9988776664,
        'FloatValue': 0.28,
        'ItemID': 110,
        'ListingID': 1009,
        'SkinName': 'AWP | Asiimov (Field-Tested)',
        'Username': 'JYniuBi'
    },
    {
        'AskingPrice': 460.0,
        'AssetID': 9988776660,
        'FloatValue': 0.005,
        'ItemID': 106,
        'ListingID': 1021,
        'SkinName': 'Glock-18 | Fade (Factory New)',
        'Username': 'JYniuBi'
    },
    {
        'AskingPrice': 145.0,
        'AssetID': 9988776655,
        'FloatValue': 0.04501234567890123,
        'ItemID': 101,
        'ListingID': 1010,
        'SkinName': 'AK-47 | Vulcan (Factory New)',
        'Username': 'Rad_atouille'
    },
    {
        'AskingPrice': 3450.0,
        'AssetID': 9988776656,
        'FloatValue': 0.2501234567890123,
        'ItemID': 102,
        'ListingID': 1011,
        'SkinName': 'AWP | Dragon Lore (Field-Tested)',
        'Username': 'Rad_atouille'
    },
    {
        'AskingPrice': 1180.0,
        'AssetID': 9988776657,
        'FloatValue': 0.01599999999999999,
        'ItemID': 103,
        'ListingID': 1012,
        'SkinName': 'Karambit | Doppler (Factory New)',
        'Username': 'Rad_atouille'
    },
    {
        'AskingPrice': 2500.0,
        'AssetID': 9988776658,
        'FloatValue': 0.11055555555555555,
        'ItemID': 104,
        'ListingID': 1013,
        'SkinName': 'M4A4 | Howl (Minimal Wear)',
        'Username': 'Rad_atouille'
    },
    {
        'AskingPrice': 300.0,
        'AssetID': 9988776659,
        'FloatValue': 0.02011111111111111,
        'ItemID': 105,
        'ListingID': 1014,
        'SkinName': 'Desert Eagle | Blaze (Factory New)',
        'Username': 'Rad_atouille'
    },
    {
        'AskingPrice': 450.0,
        'AssetID': 9988776660,
        'FloatValue': 0.005,
        'ItemID': 106,
        'ListingID': 1015,
        'SkinName': 'Glock-18 | Fade (Factory New)',
        'Username': 'Rad_atouille'
    },
    {
        'AskingPrice': 2050.0,
        'AssetID': 9988776662,
        'FloatValue': 0.03,
        'ItemID': 108,
        'ListingID': 1016,
        'SkinName': 'Butterfly Knife | Fade (Factory New)',
        'Username': 'Rad_atouille'
    },
    {
        'AskingPrice': 42.0,
        'AssetID': 9988776661,
        'FloatValue': 0.85,
        'ItemID': 107,
        'ListingID': 1025,
        'SkinName': 'USP-S | Kill Confirmed (Battle-Scarred)',
        'Username': 'Rad_atouille'
    },
    {
        'AskingPrice': 3600.0,
        'AssetID': 9988776656,
        'FloatValue': 0.2501234567890123,
        'ItemID': 102,
        'ListingID': 1017,
        'SkinName': 'AWP | Dragon Lore (Field-Tested)',
        'Username': 'IcEMaN'
    },
    {
        'AskingPrice': 90.0,
        'AssetID': 9988776664,
        'FloatValue': 0.28,
        'ItemID': 110,
        'ListingID': 1018,
        'SkinName': 'AWP | Asiimov (Field-Tested)',
        'Username': 'IcEMaN'
    },
    {
        'AskingPrice': 155.0,
        'AssetID': 9988776655,
        'FloatValue': 0.04501234567890123,
        'ItemID': 101,
        'ListingID': 1022,
        'SkinName': 'AK-47 | Vulcan (Factory New)',
        'Username': 'IcEMaN'
    },
    {
        'AskingPrice': 1250.0,
        'AssetID': 9988776657,
        'FloatValue': 0.01599999999999999,
        'ItemID': 103,
        'ListingID': 1026,
        'SkinName': 'Karambit | Doppler (Factory New)',
        'Username': 'IcEMaN'
    }
]

MOCK_ASSET_AUDIT = [
  {'AskingPrice': 1200.0,
   'AssetID': 9988776657,
   'FloatValue': 0.01599999999999999,
   'ItemID': 103,
   'LinePrice': 1200.0,
   'ListingID': 1005,
   'SkinName': 'Karambit | Doppler (Factory New)',
   'TransactionID': 5001},
  {'AskingPrice': 1180.0,
   'AssetID': 9988776657,
   'FloatValue': 0.01599999999999999,
   'ItemID': 103,
   'LinePrice': 1200.0,
   'ListingID': 1012,
   'SkinName': 'Karambit | Doppler (Factory New)',
   'TransactionID': 5001},
  {'AskingPrice': 1250.0,
   'AssetID': 9988776657,
   'FloatValue': 0.01599999999999999,
   'ItemID': 103,
   'LinePrice': 1200.0,
   'ListingID': 1026,
   'SkinName': 'Karambit | Doppler (Factory New)',
   'TransactionID': 5001},
  {'AskingPrice': 85.0,
   'AssetID': 9988776664,
   'FloatValue': 0.28,
   'ItemID': 110,
   'LinePrice': 85.0,
   'ListingID': 1003,
   'SkinName': 'AWP | Asiimov (Field-Tested)',
   'TransactionID': 5002},
  {'AskingPrice': 80.0,
   'AssetID': 9988776664,
   'FloatValue': 0.28,
   'ItemID': 110,
   'LinePrice': 85.0,
   'ListingID': 1009,
   'SkinName': 'AWP | Asiimov (Field-Tested)',
   'TransactionID': 5002},
  {'AskingPrice': 90.0,
   'AssetID': 9988776664,
   'FloatValue': 0.28,
   'ItemID': 110,
   'LinePrice': 85.0,
   'ListingID': 1018,
   'SkinName': 'AWP | Asiimov (Field-Tested)',
   'TransactionID': 5002},
  {'AskingPrice': 300.0,
   'AssetID': 9988776659,
   'FloatValue': 0.02011111111111111,
   'ItemID': 105,
   'LinePrice': 300.0,
   'ListingID': 1014,
   'SkinName': 'Desert Eagle | Blaze (Factory New)',
   'TransactionID': 5003},
  {'AskingPrice': 310.0,
   'AssetID': 9988776659,
   'FloatValue': 0.02011111111111111,
   'ItemID': 105,
   'LinePrice': 300.0,
   'ListingID': 1020,
   'SkinName': 'Desert Eagle | Blaze (Factory New)',
   'TransactionID': 5003},
  {'AskingPrice': 25.5,
   'AssetID': 9988776663,
   'FloatValue': 0.22,
   'ItemID': 109,
   'LinePrice': 25.5,
   'ListingID': 1002,
   'SkinName': 'AK-47 | Redline (Field-Tested)',
   'TransactionID': 5004},
  {'AskingPrice': 24.0,
   'AssetID': 9988776663,
   'FloatValue': 0.22,
   'ItemID': 109,
   'LinePrice': 25.5,
   'ListingID': 1008,
   'SkinName': 'AK-47 | Redline (Field-Tested)',
   'TransactionID': 5004},
  {'AskingPrice': 26.0,
   'AssetID': 9988776663,
   'FloatValue': 0.22,
   'ItemID': 109,
   'LinePrice': 25.5,
   'ListingID': 1024,
   'SkinName': 'AK-47 | Redline (Field-Tested)',
   'TransactionID': 5004},
  {'AskingPrice': 150.0,
   'AssetID': 9988776655,
   'FloatValue': 0.04501234567890123,
   'ItemID': 101,
   'LinePrice': None,
   'ListingID': 1001,
   'SkinName': 'AK-47 | Vulcan (Factory New)',
   'TransactionID': None},
  {'AskingPrice': 145.0,
   'AssetID': 9988776655,
   'FloatValue': 0.04501234567890123,
   'ItemID': 101,
   'LinePrice': None,
   'ListingID': 1010,
   'SkinName': 'AK-47 | Vulcan (Factory New)',
   'TransactionID': None},
  {'AskingPrice': 155.0,
   'AssetID': 9988776655,
   'FloatValue': 0.04501234567890123,
   'ItemID': 101,
   'LinePrice': None,
   'ListingID': 1022,
   'SkinName': 'AK-47 | Vulcan (Factory New)',
   'TransactionID': None},
  {'AskingPrice': 3500.0,
   'AssetID': 9988776656,
   'FloatValue': 0.2501234567890123,
   'ItemID': 102,
   'LinePrice': None,
   'ListingID': 1004,
   'SkinName': 'AWP | Dragon Lore (Field-Tested)',
   'TransactionID': None},
  {'AskingPrice': 3450.0,
   'AssetID': 9988776656,
   'FloatValue': 0.2501234567890123,
   'ItemID': 102,
   'LinePrice': None,
   'ListingID': 1011,
   'SkinName': 'AWP | Dragon Lore (Field-Tested)',
   'TransactionID': None},
  {'AskingPrice': 3600.0,
   'AssetID': 9988776656,
   'FloatValue': 0.2501234567890123,
   'ItemID': 102,
   'LinePrice': None,
   'ListingID': 1017,
   'SkinName': 'AWP | Dragon Lore (Field-Tested)',
   'TransactionID': None},
  {'AskingPrice': 2500.0,
   'AssetID': 9988776658,
   'FloatValue': 0.11055555555555555,
   'ItemID': 104,
   'LinePrice': None,
   'ListingID': 1013,
   'SkinName': 'M4A4 | Howl (Minimal Wear)',
   'TransactionID': None},
  {'AskingPrice': 2400.0,
   'AssetID': 9988776658,
   'FloatValue': 0.11055555555555555,
   'ItemID': 104,
   'LinePrice': None,
   'ListingID': 1019,
   'SkinName': 'M4A4 | Howl (Minimal Wear)',
   'TransactionID': None},
  {'AskingPrice': 450.0,
   'AssetID': 9988776660,
   'FloatValue': 0.005,
   'ItemID': 106,
   'LinePrice': None,
   'ListingID': 1015,
   'SkinName': 'Glock-18 | Fade (Factory New)',
   'TransactionID': None},
  {'AskingPrice': 460.0,
   'AssetID': 9988776660,
   'FloatValue': 0.005,
   'ItemID': 106,
   'LinePrice': None,
   'ListingID': 1021,
   'SkinName': 'Glock-18 | Fade (Factory New)',
   'TransactionID': None},
  {'AskingPrice': 45.0,
   'AssetID': 9988776661,
   'FloatValue': 0.85,
   'ItemID': 107,
   'LinePrice': None,
   'ListingID': 1007,
   'SkinName': 'USP-S | Kill Confirmed (Battle-Scarred)',
   'TransactionID': None},
  {'AskingPrice': 42.0,
   'AssetID': 9988776661,
   'FloatValue': 0.85,
   'ItemID': 107,
   'LinePrice': None,
   'ListingID': 1025,
   'SkinName': 'USP-S | Kill Confirmed (Battle-Scarred)',
   'TransactionID': None},
  {'AskingPrice': 2100.0,
   'AssetID': 9988776662,
   'FloatValue': 0.03,
   'ItemID': 108,
   'LinePrice': None,
   'ListingID': 1006,
   'SkinName': 'Butterfly Knife | Fade (Factory New)',
   'TransactionID': None},
  {'AskingPrice': 2050.0,
   'AssetID': 9988776662,
   'FloatValue': 0.03,
   'ItemID': 108,
   'LinePrice': None,
   'ListingID': 1016,
   'SkinName': 'Butterfly Knife | Fade (Factory New)',
   'TransactionID': None},
  {'AskingPrice': 2150.0,
   'AssetID': 9988776662,
   'FloatValue': 0.03,
   'ItemID': 108,
   'LinePrice': None,
   'ListingID': 1023,
   'SkinName': 'Butterfly Knife | Fade (Factory New)',
   'TransactionID': None}
]

MOCK_TRANSACTIONS = [
    {
        'AssetID': 9988776657,
        'BuyerName': 'car',
        'LinePrice': 1200.0,
        'SkinName': 'Karambit | Doppler (Factory New)',
        'TimeCompleted': '2026-05-20 23:33:54',
        'TransactionID': 5001
    },
    {
        'AssetID': 9988776664,
        'BuyerName': 'potsu_420',
        'LinePrice': 85.0,
        'SkinName': 'AWP | Asiimov (Field-Tested)',
        'TimeCompleted': '2026-05-20 23:33:54',
        'TransactionID': 5002
    },
    {
        'AssetID': 9988776659,
        'BuyerName': 'JYniuBi',
        'LinePrice': 300.0,
        'SkinName': 'Desert Eagle | Blaze (Factory New)',
        'TimeCompleted': '2026-05-20 23:33:54',
        'TransactionID': 5003
    },
    {
        'AssetID': 9988776663,
        'BuyerName': 'IcEMaN',
        'LinePrice': 25.5,
        'SkinName': 'AK-47 | Redline (Field-Tested)',
        'TimeCompleted': '2026-05-20 23:33:54',
        'TransactionID': 5004
    }
]

MOCK_TRADERS = [
    {
        'ActiveListings': 1,
        'AssetID': 9988776655,
        'LastActive': '2026-05-18',
        'SteamID64': 76561198200000001,
        'TotalTrades': 15,
        'TraderID': 1,
        'Username': 'car'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776658,
        'LastActive': '2026-05-18',
        'SteamID64': 76561198200000001,
        'TotalTrades': 15,
        'TraderID': 1,
        'Username': 'car'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776662,
        'LastActive': '2026-05-18',
        'SteamID64': 76561198200000001,
        'TotalTrades': 15,
        'TraderID': 1,
        'Username': 'car'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776663,
        'LastActive': '2026-05-18',
        'SteamID64': 76561198200000001,
        'TotalTrades': 15,
        'TraderID': 1,
        'Username': 'car'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776664,
        'LastActive': '2026-05-18',
        'SteamID64': 76561198200000001,
        'TotalTrades': 15,
        'TraderID': 1,
        'Username': 'car'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776656,
        'LastActive': '2026-05-19',
        'SteamID64': 76561198000320002,
        'TotalTrades': 42,
        'TraderID': 2,
        'Username': 'potsu_420'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776657,
        'LastActive': '2026-05-19',
        'SteamID64': 76561198000320002,
        'TotalTrades': 42,
        'TraderID': 2,
        'Username': 'potsu_420'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776659,
        'LastActive': '2026-05-19',
        'SteamID64': 76561198000320002,
        'TotalTrades': 42,
        'TraderID': 2,
        'Username': 'potsu_420'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776662,
        'LastActive': '2026-05-19',
        'SteamID64': 76561198000320002,
        'TotalTrades': 42,
        'TraderID': 2,
        'Username': 'potsu_420'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776663,
        'LastActive': '2026-05-19',
        'SteamID64': 76561198000320002,
        'TotalTrades': 42,
        'TraderID': 2,
        'Username': 'potsu_420'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776660,
        'LastActive': '2026-05-10',
        'SteamID64': 76561198004500003,
        'TotalTrades': 5,
        'TraderID': 3,
        'Username': 'JYniuBi'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776661,
        'LastActive': '2026-05-10',
        'SteamID64': 76561198004500003,
        'TotalTrades': 5,
        'TraderID': 3,
        'Username': 'JYniuBi'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776663,
        'LastActive': '2026-05-10',
        'SteamID64': 76561198004500003,
        'TotalTrades': 5,
        'TraderID': 3,
        'Username': 'JYniuBi'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776664,
        'LastActive': '2026-05-10',
        'SteamID64': 76561198004500003,
        'TotalTrades': 5,
        'TraderID': 3,
        'Username': 'JYniuBi'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776655,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198400000004,
        'TotalTrades': 1250,
        'TraderID': 4,
        'Username': 'Rad_atouille'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776656,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198400000004,
        'TotalTrades': 1250,
        'TraderID': 4,
        'Username': 'Rad_atouille'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776657,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198400000004,
        'TotalTrades': 1250,
        'TraderID': 4,
        'Username': 'Rad_atouille'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776658,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198400000004,
        'TotalTrades': 1250,
        'TraderID': 4,
        'Username': 'Rad_atouille'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776659,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198400000004,
        'TotalTrades': 1250,
        'TraderID': 4,
        'Username': 'Rad_atouille'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776660,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198400000004,
        'TotalTrades': 1250,
        'TraderID': 4,
        'Username': 'Rad_atouille'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776661,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198400000004,
        'TotalTrades': 1250,
        'TraderID': 4,
        'Username': 'Rad_atouille'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776662,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198400000004,
        'TotalTrades': 1250,
        'TraderID': 4,
        'Username': 'Rad_atouille'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776655,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198000066005,
        'TotalTrades': 22,
        'TraderID': 5,
        'Username': 'IcEMaN'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776656,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198000066005,
        'TotalTrades': 22,
        'TraderID': 5,
        'Username': 'IcEMaN'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776657,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198000066005,
        'TotalTrades': 22,
        'TraderID': 5,
        'Username': 'IcEMaN'
    },
    {
        'ActiveListings': 1,
        'AssetID': 9988776664,
        'LastActive': '2026-05-20',
        'SteamID64': 76561198000066005,
        'TotalTrades': 22,
        'TraderID': 5,
        'Username': 'IcEMaN'
    }
]

# Check active database connection
use_mock = False
try:
    conn = get_db_connection()
    conn.close()
    st.sidebar.success("✅ MySQL Database Connected")
except Exception as e:
    use_mock = True
    st.sidebar.warning("⚠️ Running in Offline Demo Mode")
    st.sidebar.caption("Could not connect to MySQL server. Using mock tables instead.")

# Load semi-structured file store
json_store = load_json_data()

# ==========================================================================
# UI Layout
# ==========================================================================

st.title("🎮 CS-Nexus: Hybrid Marketplace Datastore")
st.caption("Fundamentals of Data Management - Project Phase 5 (Distinction Project)")
st.write("---")

# Task I-A: Basic Role-Based Access Control
role = st.sidebar.selectbox("Select Your Access Role:", ["User Mode", "Admin Mode"])

# Lock Admin Mode with a password gate
admin_authenticated = False
if role == "Admin Mode":
    admin_passkey = st.sidebar.text_input("Enter Admin Passkey:", type="password")
    if admin_passkey == "admin123":
        admin_authenticated = True
        st.sidebar.success("🔒 Admin Access Granted")
    else:
        if admin_passkey != "":
            st.sidebar.error("❌ Access Denied: Incorrect Passkey")
else:
    admin_authenticated = True

st.sidebar.info(f"Current Access Level: **{role if admin_authenticated else 'Unauthenticated'}**")

# Helper function to render Report 1 (Active Listings Catalog)
def render_report_1():
    st.subheader("Report 1: Active Listings Catalog")
    st.write("This report compiles real-time extraction across all three data representations simultaneously (structured tables, JSON stickers, and local screenshot imagery files).")
    st.write("---")

    listings = []
    
    if use_mock:
        listings = MOCK_LISTINGS
    else:
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            
            # Structured component: joining 3 entities (TradeListing, Trader, SkinItem)
            query = """
                SELECT l.ListingID, t.Username, s.ItemID, s.AssetID, s.SkinName, s.FloatValue, l.AskingPrice 
                FROM TradeListing l
                JOIN Trader t ON l.TraderID = t.TraderID
                JOIN SkinItem s ON l.ItemID = s.ItemID;
            """
            cursor.execute(query)
            listings = cursor.fetchall()
            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"Failed to load database structures: {e}")
            listings = []

    if listings:
        for item in listings:
            # Visual card layout
            with st.container():
                col1, col2, col3 = st.columns([1, 2, 2])
                
                asset_id_str = str(item['AssetID'])
                
                # Unstructured Component Check: Render image if path exists
                img_path = f"data_store/screenshots/{asset_id_str}.png"
                with col1:
                    if os.path.exists(img_path):
                        st.image(img_path, use_container_width=True)
                    else:
                        st.warning("⚠️ Image Missing")
                
                # Structured Components Section
                with col2:
                    st.subheader(item['SkinName'])
                    st.write(f"👤 **Seller:** {item['Username']}")
                    st.write(f"📉 **Wear Float:** {float(item['FloatValue']):.5f}")
                    st.metric(label="Price (RM)", value=f"RM {float(item['AskingPrice']):,.2f}")
                
                # Semi-Structured Component Check: Fetch metadata attributes via JSON key
                with col3:
                    st.write("✨ **Applied Modifications (JSON Metadata):**")
                    if asset_id_str in json_store:
                        custom_details = json_store[asset_id_str]
                        st.write(f"🏷️ *Custom Nametag:* `{custom_details.get('custom_nametag', 'None')}`")
                        
                        stickers = custom_details.get("stickers", [])
                        if stickers:
                            for stkr in stickers:
                                st.caption(f"▪️ {stkr['name']} (Condition: {stkr['wear'] * 100:.0f}% worn)")
                        else:
                            st.write("*No stickers applied to this weapon asset.*")
                    else:
                        st.write("*No custom modification layout found in semi-structured storage.*")
            st.write("---")
    else:
        st.info("No active listings currently populated in the database tables.")

# ==================== USER MODE ====================
if role == "User Mode":
    st.header("🛒 User Mode: Active Showcase Dashboard")
    render_report_1()

# ==================== ADMIN MODE ====================
elif role == "Admin Mode":
    if not admin_authenticated:
        st.header("📊 Admin Mode: Platform Analytical Dashboard")
        st.info("🔒 Please enter the correct **Admin Passkey** in the sidebar to view platform reports.")
    else:
        st.header("📊 Admin Mode: Platform Analytical Dashboard")
        
        # Let admin select between the three reports
        admin_tab = st.selectbox("Select Report Module:", [
            "Report 1: System Asset Valuation & Pricing Volatility Audit",
            "Report 2: Completed Transactions Ledger",
            "Report 3: Trader Performance & Volumetric Analysis"
        ])
        st.write("---")
        
        # -------------------- REPORT 1: SYSTEM ASSET VALUATION & PRICING VOLATILITY AUDIT --------------------
        if admin_tab == "Report 1: System Asset Valuation & Pricing Volatility Audit":
            st.subheader("Report 1: System Asset Valuation & Pricing Volatility Audit")
            st.write("This report compiles registered skin items, merging active market listings with historic transactions to audit variance between asking prices and sold prices.")
            
            df_audit = pd.DataFrame()
            if use_mock:
                df_audit = pd.DataFrame(MOCK_ASSET_AUDIT)
            else:
                try:
                    conn = get_db_connection()
                    audit_query = """
                        SELECT 
                            s.ItemID, 
                            s.AssetID, 
                            s.SkinName, 
                            s.FloatValue,
                            l.ListingID,
                            l.AskingPrice,
                            ti.TransactionID,
                            ti.LinePrice
                        FROM SkinItem s
                        LEFT JOIN TradeListing l ON s.ItemID = l.ItemID
                        LEFT JOIN TransactionItem ti ON s.ItemID = ti.ItemID;
                    """
                    df_audit = pd.read_sql(audit_query, conn)
                    conn.close()
                except Exception as e:
                    st.error(f"Error compiling asset valuation reports: {e}")
                    df_audit = pd.DataFrame()

            if not df_audit.empty:
                # Type conversions
                df_audit['AssetID'] = df_audit['AssetID'].astype(str)
                df_audit['FloatValue'] = df_audit['FloatValue'].astype(float)
                df_audit['AskingPrice'] = df_audit['AskingPrice'].astype(float)
                df_audit['LinePrice'] = df_audit['LinePrice'].astype(float)
                
                # Hybrid integration details
                df_audit['Custom Nametag'] = df_audit['AssetID'].apply(
                    lambda x: json_store.get(x, {}).get('custom_nametag', 'None')
                )
                df_audit['Sticker Count'] = df_audit['AssetID'].apply(
                    lambda x: len(json_store.get(x, {}).get('stickers', []))
                )
                df_audit['Screenshot Status'] = df_audit['AssetID'].apply(
                    lambda x: "Present" if os.path.exists(f"data_store/screenshots/{x}.png") else "Missing"
                )
                
                # Compute Price Volatility / Markup: (AskingPrice - LinePrice) / LinePrice
                def compute_variance(row):
                    if pd.isna(row['AskingPrice']) or pd.isna(row['LinePrice']) or row['LinePrice'] == 0:
                        return "N/A"
                    var = ((row['AskingPrice'] - row['LinePrice']) / row['LinePrice']) * 100
                    return f"{var:+.1f}%"
                
                df_audit['Price Variance'] = df_audit.apply(compute_variance, axis=1)

                # Format display columns
                df_audit['Asking Price'] = df_audit['AskingPrice'].apply(lambda x: f"RM {x:,.2f}" if not pd.isna(x) else "Not Listed")
                df_audit['Sold Price'] = df_audit['LinePrice'].apply(lambda x: f"RM {x:,.2f}" if not pd.isna(x) else "Not Sold")

                # Controls
                st.write("#### Report Controls")
                col_ctrl1, col_ctrl2 = st.columns(2)
                with col_ctrl1:
                    wear_filter = st.slider("Filter by maximum item wear float value:", 0.0, 1.0, 1.0)
                with col_ctrl2:
                    sort_order = st.selectbox("Sort records by:", ["Skin Name", "Asking Price (High-Low)", "Wear Float (Low-High)"])

                # Filter
                filtered_df = df_audit[df_audit['FloatValue'] <= wear_filter]
                
                # Sort
                if sort_order == "Skin Name":
                    filtered_df = filtered_df.sort_values(by="SkinName")
                elif sort_order == "Asking Price (High-Low)":
                    filtered_df = filtered_df.sort_values(by="AskingPrice", ascending=False, na_position='last')
                elif sort_order == "Wear Float (Low-High)":
                    filtered_df = filtered_df.sort_values(by="FloatValue")

                # Columns for display
                display_cols = [
                    'SkinName', 'AssetID', 'FloatValue', 'Asking Price', 'Sold Price', 
                    'Price Variance', 'Custom Nametag', 'Sticker Count', 'Screenshot Status'
                ]
                
                st.write("#### System Asset Audit Ledger")
                st.dataframe(filtered_df[display_cols], use_container_width=True)

                # CSV Download
                csv_bytes = filtered_df[display_cols].to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Export Valuation Report to CSV Format",
                    data=csv_bytes,
                    file_name="cs_nexus_asset_valuation_report.csv",
                    mime="text/csv"
                )
            else:
                st.info("No system assets to audit yet.")
            
        # -------------------- REPORT 2: COMPLETED TRANSACTIONS LEDGER --------------------
        elif admin_tab == "Report 2: Completed Transactions Ledger":
            st.subheader("Report 2: Completed Transactions Ledger")
            st.write("This report compiles structured transaction tables enriched dynamically with semi-structured nametag modifications and unstructured screenshot availability audits.")
            
            df_report = pd.DataFrame()
            
            if use_mock:
                df_report = pd.DataFrame(MOCK_TRANSACTIONS)
            else:
                try:
                    conn = get_db_connection()
                    # Structured component: joining 4 entities (TransactionItem, TradeTransaction, Trader, SkinItem)
                    report_query = """
                        SELECT ti.TransactionID, t.Username as BuyerName, s.SkinName, s.AssetID, ti.LinePrice, tr.TimeCompleted
                        FROM TransactionItem ti
                        JOIN TradeTransaction tr ON ti.TransactionID = tr.TransactionID
                        JOIN Trader t ON tr.BuyerID = t.TraderID
                        JOIN SkinItem s ON ti.ItemID = s.ItemID;
                    """
                    df_report = pd.read_sql(report_query, conn)
                    conn.close()
                except Exception as e:
                    st.error(f"Error compiling administrative reports: {e}")
                    df_report = pd.DataFrame()

            if not df_report.empty:
                # Enforce string representations for lookups
                df_report['AssetID'] = df_report['AssetID'].astype(str)
                
                # Hybrid Data Enrichment Steps
                # 1. Parse JSON semi-structured nametag
                df_report['Custom Nametag'] = df_report['AssetID'].apply(
                    lambda x: json_store.get(x, {}).get('custom_nametag', 'None')
                )
                # 2. Check Unstructured folder screenshot file status
                df_report['Screenshot Present'] = df_report['AssetID'].apply(
                    lambda x: "Yes" if os.path.exists(f"data_store/screenshots/{x}.png") else "No"
                )
                
                # Sidebar interactive filtering and sorting (Task II-B)
                st.write("#### Report Controls")
                col_ctrl1, col_ctrl2 = st.columns(2)
                with col_ctrl1:
                    max_price = float(df_report["LinePrice"].max())
                    price_filter = st.slider("Filter results by maximum transaction item price:", 0.0, max_price, max_price)
                with col_ctrl2:
                    sort_order = st.selectbox("Sort records chronologically by timestamp order:", ["Descending (Newest)", "Ascending (Oldest)"])

                # Filter data array matrix
                filtered_df = df_report[df_report["LinePrice"] <= price_filter]
                
                # Sort data array matrix
                ascending_bool = True if sort_order == "Ascending (Oldest)" else False
                filtered_df = filtered_df.sort_values(by="TimeCompleted", ascending=ascending_bool)

                # Display final combined report
                st.write("#### Compiled Records")
                st.dataframe(filtered_df, use_container_width=True)

                # Task II-C: Export function to standard CSV
                csv_bytes = filtered_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Export Report to CSV Format",
                    data=csv_bytes,
                    file_name="cs_nexus_transaction_report.csv",
                    mime="text/csv"
                )
            else:
                st.info("The system transaction logs do not contain any recorded histories yet.")

        # -------------------- REPORT 3: TRADER PERFORMANCE REPORT --------------------
        elif admin_tab == "Report 3: Trader Performance & Volumetric Analysis":
            st.subheader("Report 3: Trader Performance & Volumetric Analysis")
            st.write("This report compiles structured stats tables joined with listing counts, and aggregates JSON customizations (sticker count) and file audits (screenshot ratio) per user.")
            
            df_trader = pd.DataFrame()
            
            if use_mock:
                df_trader = pd.DataFrame(MOCK_TRADERS)
            else:
                try:
                    conn = get_db_connection()
                    # Structured component: joining 3 entities (Trader, TraderStats, TradeListing count)
                    trader_query = """
                        SELECT t.TraderID, t.Username, t.SteamID64, ts.TotalTrades, ts.LastActive, COUNT(l.ListingID) as ActiveListings, s.AssetID
                        FROM Trader t
                        LEFT JOIN TraderStats ts ON t.TraderID = ts.TraderID
                        LEFT JOIN TradeListing l ON t.TraderID = l.TraderID
                        LEFT JOIN SkinItem s ON l.ItemID = s.ItemID
                        GROUP BY t.TraderID, t.Username, t.SteamID64, ts.TotalTrades, ts.LastActive, s.AssetID;
                    """
                    # Note: We query AssetID to help aggregate lookup values in pandas
                    df_trader = pd.read_sql(trader_query, conn)
                    conn.close()
                except Exception as e:
                    st.error(f"Error compiling trader reports: {e}")
                    df_trader = pd.DataFrame()

            if not df_trader.empty:
                # Fill missing entries
                df_trader['ActiveListings'] = df_trader['ActiveListings'].fillna(0).astype(int)
                df_trader['TotalTrades'] = df_trader['TotalTrades'].fillna(0).astype(int)
                df_trader['LastActive'] = df_trader['LastActive'].fillna("N/A")
                
                # Hybrid Data Enrichment:
                # 1. Check custom JSON stickers applied to trader active listings
                def get_sticker_count(asset_id):
                    if pd.isna(asset_id):
                        return 0
                    asset_str = str(int(float(asset_id)))
                    return len(json_store.get(asset_str, {}).get('stickers', []))

                df_trader['Sticker Modifications'] = df_trader['AssetID'].apply(get_sticker_count)

                # 2. Check screenshot file availability in folders
                def check_screenshot_present(asset_id):
                    if pd.isna(asset_id):
                        return "No Listing"
                    asset_str = str(int(float(asset_id)))
                    return "Uploaded" if os.path.exists(f"data_store/screenshots/{asset_str}.png") else "Missing"

                df_trader['Screenshots Status'] = df_trader['AssetID'].apply(check_screenshot_present)

                # Group duplicates if SQL returns multiple listings per trader
                df_trader_grouped = df_trader.groupby(['TraderID', 'Username', 'SteamID64', 'TotalTrades', 'LastActive']).agg({
                    'ActiveListings': 'sum',
                    'Sticker Modifications': 'sum',
                    'Screenshots Status': lambda x: ", ".join(set(x))
                }).reset_index()

                # Filters & Controls
                st.write("#### Report Controls")
                min_trades = st.number_input("Minimum Completed Trades Filter:", min_value=0, value=0)
                sort_by_column = st.selectbox("Sort table rows by field:", ["TotalTrades", "ActiveListings", "Username"])
                
                filtered_traders = df_trader_grouped[df_trader_grouped["TotalTrades"] >= min_trades]
                filtered_traders = filtered_traders.sort_values(by=sort_by_column, ascending=False if sort_by_column != "Username" else True)

                # Display final combined report
                st.write("#### Trader Performance Records")
                st.dataframe(filtered_traders, use_container_width=True)

                # CSV download button for Report 3
                csv_bytes = filtered_traders.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Export Report 3 to CSV Format",
                    data=csv_bytes,
                    file_name="cs_nexus_trader_performance_report.csv",
                    mime="text/csv"
                )
            else:
                st.info("No trader profiling logs found in database.")
