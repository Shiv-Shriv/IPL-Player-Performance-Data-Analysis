
from processing.data_loader import load_data

matches, deliveries = load_data()

playerdelivery_list = []

playerdelivery_list.extend(deliveries["batsman"])
playerdelivery_list.extend(deliveries["bowler"])

player_set = set(playerdelivery_list)

player_list = list(player_set)

player_list.sort()

def contains_player_substring(query):
    querylower = query.lower()

    potential_searches = []
    for player in player_list:
        playerlower = player.lower()
        if querylower in playerlower:
            potential_searches.append(player)
            
    return potential_searches

