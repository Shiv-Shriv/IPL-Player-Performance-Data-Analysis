import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_data():
    matches = pd.read_csv(os.path.join(BASE_DIR, "data", "matches_updated_ipl_upto_2025.csv"))
    deliveries = pd.read_csv(os.path.join(BASE_DIR, "data", "deliveries_updated_ipl_upto_2025.csv"))
    
    deliveries["total_runs"] = deliveries["batsman_runs"] + deliveries["extras"]
    deliveries["date"] = pd.to_datetime(deliveries["date"])
    return matches, deliveries