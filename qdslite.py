import sqlite3
import pandas as pd

# Load the CSV file with classified intents
csv_file_path = "home_appliance_summary_labeled.csv"
df = pd.read_csv(csv_file_path)

# Connect to SQLite Database
conn = sqlite3.connect("home_appliance.db")
cursor = conn.cursor()

# Function to process intent and generate SQL queries
def process_intent(appliance, user_query, intent_index):
    if intent_index == 0:  # Troubleshooting
        print(f"🔍 Searching for troubleshooting steps for {appliance}...")
        sql_query = "SELECT solution FROM troubleshooting WHERE appliance = ? AND issue LIKE ?"
        cursor.execute(sql_query, (appliance, f"%{user_query}%"))
        result = cursor.fetchone()
        return result[0] if result else "No troubleshooting steps found."

    elif intent_index == 1:  # General Inquiry
        print(f"ℹ️ Fetching general information...")
        sql_query = "SELECT answer FROM general_inquiries WHERE question LIKE ?"
        cursor.execute(sql_query, (f"%{user_query}%",))
        result = cursor.fetchone()
        return result[0] if result else "No relevant information found."

    elif intent_index == 2:  # Repair Request
        print(f"🛠️ Logging a repair request for {appliance}...")
        sql_query = "INSERT INTO repair_requests (appliance, user_issue) VALUES (?, ?)"
        cursor.execute(sql_query, (appliance, user_query))
        conn.commit()
        return "Repair request successfully logged."

    else:
        return "Unknown intent."

# Process each row in the CSV file
for index, row in df.iterrows():
    appliance = row["appliance"]
    user_query = row["user_query"]
    intent_index = row["label"]  # 0, 1, or 2

    response = process_intent(appliance, user_query, intent_index)
    print(f"Response: {response}")

# Close database connection
conn.close()

print("✅ Text-to-SQL processing completed!")
