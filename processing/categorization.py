import pandas as pd
from processing.data_loader import load_data

matches, deliveries = load_data()


legal_bf = deliveries[deliveries["isWide"].isna()]
balls_faced = legal_bf.groupby("batsman").size()
maximum_bf = balls_faced.max()


legal_bb = deliveries[(deliveries["isWide"].isna())&(deliveries["isNoBall"].isna())]
balls_bowled = legal_bb.groupby("bowler").size()
maximum_bb = balls_bowled.max()

def get_player_category(player_name):
    player_bf = balls_faced.get(player_name, 0)
    player_bb = balls_bowled.get(player_name, 0)

    normalised_bf = player_bf/maximum_bf
    normalised_bb = player_bb/maximum_bb
 
    if((player_bf>=250)and(player_bb<100)):
        return "Batter"
    elif((player_bf<250)and(player_bb>=100)):
        return "Bowler"
    elif((player_bf>=250)and(player_bb>=100)):
        if(normalised_bb>normalised_bf):
            return "Bowling All-Rounder"
        else:
            return "Batting All-Rounder"

    else:
        return "Unclassified"

    


