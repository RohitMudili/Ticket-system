import os

print("🚀 Starting Home Appliance Workflow...")

# 1️⃣ Summarization Step
print("\n📝 Step 1: Summarizing Responses...")
os.system("python summarize_home_appliance.py")

# 2️⃣ Intent Classification and Database Storage
print("\n🔍 Step 2: Intent Classification & Storing Data into Database...")
os.system("python qdslite.py")

# 3️⃣ Query Database and Create Tables
print("\n📊 Step 3: Setting Up SQLite Tables...")
os.system("python query_database.py")

# 4️⃣ Schedule Emails for Maintenance Requests
print("\n📩 Step 4: Scheduling Emails for Maintenance Requests...")
os.system("python SE.py")

# 5️⃣ Trigger AI Agent for Email Notification
print("\n📧 Step 5: Triggering Email Notification AI Agent...")
os.system("python test.py")

print("\n✅ Home Appliance AI Pipeline Completed Successfully!")
