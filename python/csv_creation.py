import re
import pandas as pd

input_text = """
"""

# Split the input text into individual entries
entries = re.split(r'\d+\s*:\s*\n', input_text)

# Initialize an empty list to store the formatted data
data = []

# Loop through the entries and extract information
for entry in entries:
    if not entry.strip():
        continue  # Skip empty entries
    
    entry = entry.strip()
    name = re.search(r"name:\s*'([^']+)'", entry).group(1)
    email = re.search(r"email:\s*'([^']+)'", entry).group(1)
    phone = re.search(r"phone:\s*'([^']+)'", entry).group(1)
    
    company = "The Agency RE"

    formatted_entry = {
        'name': name,
        'email': email,
        'phone': phone,
        'Name - Company': company,
    }
    
    data.append(formatted_entry)

# Define your data as a list of dictionaries
existing_data = []

formatted_data = existing_data + data

# Print the formatted data
for i, entry in enumerate(formatted_data):
    print(f"{i}:")
    print(entry)

# Create a DataFrame from the data
df = pd.DataFrame(formatted_data)

# Drop rows with undefined values (NaN or empty strings)
df = df.dropna(subset=['name', 'email', 'phone'])

# Specify the output CSV file path
output_csv = 'california_second_part.csv'

# Save the cleaned DataFrame to a CSV file
df.to_csv(output_csv, index=False)

print(f"Cleaned data saved to '{output_csv}'")
