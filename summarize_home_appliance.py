import pandas as pd
from transformers import pipeline

# Load CSV file
csv_file_path = "home_appliance_query_response.csv"  
df = pd.read_csv(csv_file_path)

# Print available columns for debugging
print("Available columns before processing:", df.columns)

# Ensure necessary columns exist
required_columns = ["user_query", "ai_response"]
for col in required_columns:
    if col not in df.columns:
        raise KeyError(f"Column '{col}' not found in the CSV file. Check column names!")

# Combine user and AI response into a single field for summarization
df["query_response"] = df["user_query"] + " " + df["ai_response"]

# Drop existing summary columns if they exist
if "summary" in df.columns:
    df.drop(columns=["summary"], inplace=True)

# Load summarization model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    tokenizer="facebook/bart-large-cnn"
)

# Function to summarize with **dynamic** max_length and min_length
def summarize_text(text):
    input_length = len(text.split())  # Get number of words in input

    # Ensure min_length and max_length are reasonable
    min_length = max(10, input_length // 2)  # At least 10 tokens or half of input
    max_length = min(max(20, input_length * 2), 50)  # At least 20 tokens, max 50

    return summarizer(text, max_length=max_length, min_length=min_length, do_sample=False, truncation=True)[0]["summary_text"]

# Apply summarization dynamically
df["summary"] = df["query_response"].apply(summarize_text)

# Save summarized data
summary_csv_path = "home_appliance_summary.csv"
df.to_csv(summary_csv_path, index=False)

print(f"✅ Summarization complete! Output saved as {summary_csv_path}")
