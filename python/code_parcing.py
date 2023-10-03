data = {
    0: {
        "name": "Aaron Leider",
        "email": "aaron.leider@theagencyre.com",
        "phone": "(310) 595-4663 License: DRE #1211739"
    },
    1: {
        "name": "Aayeesha Essue",
        "email": "aessue@theagencyre.com",
        "phone": "(424) 371-7312 License: DRE #2129008"
    },
    # Add more data entries here...
}

formatted_data = {}  # Initialize an empty dictionary to store the formatted data

for key, value in data.items():
    # Extracting name, email, and phone
    name = value["name"]
    email = value["email"]
    phone = value["phone"]
    
    # Extracting the License number if available
    license_info = None
    if "License:" in phone:
        license_info = phone.split("License:")[1].strip()
        phone = phone.split("License:")[0].strip()
    
    # Creating the formatted entry
    formatted_entry = {
        "name": name,
        "email": email,
        "phone": phone,
        "company": "The Agency RE"
    }
    
    # Adding license information if available
    if license_info:
        formatted_entry["license"] = license_info

    formatted_data[key] = formatted_entry

# Print the formatted data
for key, value in formatted_data.items():
    print(f"{key}: {value}")
