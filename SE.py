import sqlite3
import pandas as pd

# Load CSV file containing classified intents
csv_file_path = "home_appliance_summary_labeled.csv"
df = pd.read_csv(csv_file_path)

# Connect to SQLite database
conn = sqlite3.connect("home_appliance.db")
cursor = conn.cursor()

# Function to schedule an email notification
def schedule_email(recipient, subject, body):
    cursor.execute("INSERT INTO email_queue (recipient, subject, body) VALUES (?, ?, ?)", 
                   (recipient, subject, body))
    conn.commit()
    print(f"📩 Email scheduled: {subject}")

# Process repair requests (intent = 2)
for index, row in df.iterrows():
    appliance = row["appliance"]
    user_query = row["user_query"]
    intent_index = row["label"]

    if intent_index == 2:  # Repair Request
        print(f"🛠️ Scheduling email for {appliance} repair request...")

        # Static email template
        recipient = "maintenance_team@example.com"
        subject = f"🛠 Scheduled Maintenance Request for {appliance}"
        body = f"""
        A maintenance request has been logged.

        📌 **Appliance:** {appliance}
        📝 **Issue:** {user_query}
        
        Please confirm and schedule the repair.

        -- Automated System
        """

        # Schedule email in the database
        schedule_email(recipient, subject, body)

# Close database connection
conn.close()

print("✅ All repair requests processed, emails scheduled.")
