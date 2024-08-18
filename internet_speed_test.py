import speedtest
import pandas as pd
import time
from datetime import datetime
from pymongo import MongoClient

# Kết nối tới MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Thay đổi nếu MongoDB không chạy ở localhost
db = client["internet_speed_db"]
collection = db["speed_test_results"]

def test_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    results = st.results.dict()
    
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "download_speed": results["download"] / 1_000_000,  # convert to Mbps
        "upload_speed": results["upload"] / 1_000_000,  # convert to Mbps
        "ping": results["ping"]
    }

def save_to_csv(data, filename="internet_speed.csv"):
    df = pd.DataFrame([data])
    try:
        df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def save_to_mongodb(data):
    try:
        collection.insert_one(data)
        print("Data saved to MongoDB")
    except Exception as e:
        print(f"Error saving to MongoDB: {e}")

def main():
    while True:
        try:
            data = test_speed()
            save_to_csv(data)
            save_to_mongodb(data)
            print(f"Data recorded: {data}")
        except Exception as e:
            print(f"Error during speed test: {e}")
        
        # Wait for 1 hour (3600 seconds)
        time.sleep(3600)

if __name__ == "__main__":
    main()
