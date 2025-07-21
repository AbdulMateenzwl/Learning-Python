from datetime import datetime, date, timedelta

# Get current date and time
now = datetime.now()
print("Current DateTime:", now)

# Create a specific date
d = date(2025, 7, 17)
print("Specific Date:", d)

# Formatting date
print("Formatted Date:", d.strftime("%d-%m-%Y %H:%M:%S"))

# Add/Subtract days
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)
