import pandas as pd
from processing.data_loader import load_data

matches, deliveries = load_data()

legal_bf = deliveries[deliveries["isWide"].isna()]
balls_faced = legal_bf.groupby("batsman").size()
maximum_bf = balls_faced.max()


legal_bb = deliveries[deliveries["isWide"].isna() and deliveries["isNoBall"].isna()]
balls_bowled = legal_bb.groupby("bowler").size()
maximum_bb = balls_bowled.max()