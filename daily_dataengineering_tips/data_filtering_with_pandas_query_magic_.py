import pandas as pd

data = {
    'FlightNumber': ['AA123', 'DL456', 'UA789', 'AA101', 'DL202'],
    'Duration': [300, 150, 200, 180, 230],  # In minutes
    'Airline': ['American', 'Delta', 'United', 'American', 'Delta']
}

df = pd.DataFrame(data)

# Filter flights that are longer than 2 hours (120 minutes) and by specific airline
filtered_flights = df.query('(Duration > 120) & (Airline == "Delta")')
print(filtered_flights)