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
        "ListingID": 101,
        "Username": "ZywOo",
        "ItemID": 1,
        "AssetID": 12345678901234567,
        "SkinName": "AWP | Dragon Lore",
        "FloatValue": 0.08215,
        "AskingPrice": 8500.00
    },
    {
        "ListingID": 102,
        "Username": "S1mple",
        "ItemID": 2,
        "AssetID": 98765432109876543,
        "SkinName": "AK-47 | The Empress",
        "FloatValue": 0.02142,
        "AskingPrice": 120.00
    },
    {
        "ListingID": 103,
        "Username": "Dev1ce",
        "ItemID": 3,
        "AssetID": 11112222333344445,
        "SkinName": "Butterfly Knife | Fade",
        "FloatValue": 0.03451,
        "AskingPrice": 2100.00
    }
]

MOCK_TRANSACTIONS = [
    {
        "TransactionID": 501,
        "BuyerName": "Dev1ce",
        "ItemID": 1,
        "AssetID": 12345678901234567,
        "SkinName": "AWP | Dragon Lore",
        "LinePrice": 8500.00,
        "TimeCompleted": "2026-06-05 14:32:00"
    },
    {
        "TransactionID": 502,
        "BuyerName": "Ropz",
        "ItemID": 2,
        "AssetID": 98765432109876543,
        "SkinName": "AK-47 | The Empress",
        "LinePrice": 120.00,
        "TimeCompleted": "2026-06-06 09:15:00"
    },
    {
        "TransactionID": 503,
        "BuyerName": "ZywOo",
        "ItemID": 3,
        "AssetID": 11112222333344445,
        "SkinName": "Butterfly Knife | Fade",
        "LinePrice": 2100.00,
        "TimeCompleted": "2026-06-06 12:45:00"
    }
]

MOCK_TRADERS = [
    {
        "TraderID": 1,
        "Username": "ZywOo",
        "SteamID64": 76561198000000001,
        "TotalTrades": 24,
        "LastActive": "2026-06-05",
        "ActiveListings": 1,
        "AssetID": 12345678901234567
    },
    {
        "TraderID": 2,
        "Username": "S1mple",
        "SteamID64": 76561198000000002,
        "TotalTrades": 45,
        "LastActive": "2026-06-06",
        "ActiveListings": 1,
        "AssetID": 98765432109876543
    },
    {
        "TraderID": 3,
        "Username": "Dev1ce",
        "SteamID64": 76561198000000003,
        "TotalTrades": 12,
        "LastActive": "2026-06-03",
        "ActiveListings": 1,
        "AssetID": 11112222333344445
    },
    {
        "TraderID": 4,
        "Username": "Ropz",
        "SteamID64": 76561198000000004,
        "TotalTrades": 8,
        "LastActive": "2026-06-06",
        "ActiveListings": 0,
        "AssetID": None
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

# ==================== USER MODE ====================
if role == "User Mode":
    st.header("🛒 User Mode: Active Showcase Dashboard")
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
            
            # Structured component: joining 3 entities (tradelisting, trader, skinitem)
            query = """
                SELECT l.ListingID, t.Username, s.ItemID, s.AssetID, s.SkinName, s.FloatValue, l.AskingPrice 
                FROM tradelisting l
                JOIN trader t ON l.TraderID = t.TraderID
                JOIN skinitem s ON l.ItemID = s.ItemID;
            """
            cursor.execute(query)
            listings = cursor.fetchall()
            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f"Failed to load data structures from database: {e}")
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
                        st.warning("⚠️ Screenshot File Missing")
                
                # Structured Components Section
                with col2:
                    st.subheader(item['SkinName'])
                    st.write(f"👤 **Seller:** {item['Username']}")
                    st.write(f"📉 **Wear Float Value:** `{float(item['FloatValue']):.5f}`")
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
                                st.caption(f"▪️ {stkr['name']} (Condition: {stkr['wear'] * 100:.0f}% worn, Value: ${stkr.get('value_usd', 0):,.2f})")
                        else:
                            st.write("*No stickers applied to this weapon asset.*")
                    else:
                        st.write("*No custom modification layout found in semi-structured storage.*")
            st.write("---")
    else:
        st.info("No active listings currently populated in the database tables.")

# ==================== ADMIN MODE ====================
elif role == "Admin Mode":
    if not admin_authenticated:
        st.header("📊 Admin Mode: Platform Analytical Dashboard")
        st.info("🔒 Please enter the correct **Admin Passkey** in the sidebar to view platform reports.")
    else:
        st.header("📊 Admin Mode: Platform Analytical Dashboard")
    
    # Let admin select between the two admin reports
    admin_tab = st.selectbox("Select Report Module:", ["Report 2: Completed Transactions Ledger", "Report 3: Trader Performance & Volumetric Analysis"])
    st.write("---")
    
    # -------------------- REPORT 2: COMPLETED TRANSACTIONS LEDGER --------------------
    if admin_tab == "Report 2: Completed Transactions Ledger":
        st.subheader("Platform Transaction Ledger & Sales History")
        st.write("This report compiles structured transaction tables enriched dynamically with semi-structured nametag modifications and unstructured screenshot availability audits.")
        
        df_report = pd.DataFrame()
        
        if use_mock:
            df_report = pd.DataFrame(MOCK_TRANSACTIONS)
        else:
            try:
                conn = get_db_connection()
                # Structured component: joining 4 entities (transactionitem, tradetransaction, trader, skinitem)
                report_query = """
                    SELECT ti.TransactionID, t.Username as BuyerName, s.SkinName, s.AssetID, ti.LinePrice, tr.TimeCompleted
                    FROM transactionitem ti
                    JOIN tradetransaction tr ON ti.TransactionID = tr.TransactionID
                    JOIN trader t ON tr.BuyerID = t.TraderID
                    JOIN skinitem s ON ti.ItemID = s.ItemID;
                """
                df_report = pd.read_sql(report_query, conn)
                conn.close()
            except Exception as e:
                st.error(f"Error compiling transactional report: {e}")
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
                price_filter = st.slider("Filter results by maximum transaction item price (RM):", 0.0, max_price, max_price)
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
        st.subheader("Trader Performance & Inventory Auditing Ledger")
        st.write("This report compiles structured stats tables joined with listing counts, and aggregates JSON customizations (sticker count) and file audits (screenshot ratio) per user.")
        
        df_trader = pd.DataFrame()
        
        if use_mock:
            df_trader = pd.DataFrame(MOCK_TRADERS)
        else:
            try:
                conn = get_db_connection()
                # Structured component: joining 3 entities (trader, traderstats, tradelisting count)
                trader_query = """
                    SELECT t.TraderID, t.Username, t.SteamID64, ts.TotalTrades, ts.LastActive, COUNT(l.ListingID) as ActiveListings, s.AssetID
                    FROM trader t
                    LEFT JOIN traderstats ts ON t.TraderID = ts.TraderID
                    LEFT JOIN tradelisting l ON t.TraderID = l.TraderID
                    LEFT JOIN skinitem s ON l.ItemID = s.ItemID
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
