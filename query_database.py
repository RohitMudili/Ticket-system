import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("home_appliance.db")
cursor = conn.cursor()

# Create tables if they don’t exist
cursor.execute('''CREATE TABLE IF NOT EXISTS troubleshooting (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    appliance TEXT,
                    issue TEXT,
                    solution TEXT
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS general_inquiries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT,
                    answer TEXT
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS repair_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    appliance TEXT,
                    user_issue TEXT,
                    status TEXT DEFAULT 'Pending',
                    tenant_name TEXT,
                    property_address TEXT,
                    scheduled_date TEXT
                 )''')
# Create an email queue table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS email_queue (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipient TEXT,
                    subject TEXT,
                    body TEXT,
                    status TEXT DEFAULT 'Scheduled'
                 )''')

conn.commit()
conn.close()

print("✅ Email queue table setup completed.")

print("✅ SQLite database setup complete!")
