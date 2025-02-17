import time
from functools import lru_cache

@lru_cache(maxsize=100)
def fetch_data_from_db(record_id):
    # Simulate a DB call with time delay
    print(f"Fetching record {record_id}")
    time.sleep(2)
    return f"Data for record {record_id}"

start_time = time.time()
# Fetch data for records, some repeated
data1 = fetch_data_from_db(1)
data2 = fetch_data_from_db(2)
data3 = fetch_data_from_db(1)  # Cached result

print(f"Data1: {data1}, Data2: {data2}, Data3: {data3}")
print(f"Duration: {time.time() - start_time}s")