import pandas as pd
from processing.data_loader import load_data

matches, deliveries = load_data()

def get_player_stats(player_name):
    max_year = deliveries["date"].dt.year.max()
    recent_years = [max_year, max_year - 1, max_year - 2]

    batter_data = deliveries[deliveries["batsman"] == player_name]
    bowler_data = deliveries[deliveries["bowler"] == player_name]

    recent_batter_data = batter_data[batter_data["date"].dt.year.isin(recent_years)]
    recent_bowler_data = bowler_data[bowler_data["date"].dt.year.isin(recent_years)]

    def batting_stats(data):
        balls_faced = data[data["isWide"].isna()]
        runs = data["batsman_runs"].sum()
        deliveries_faced = len(balls_faced)
        innings_played = data["matchId"].nunique()
        dismissals = data[data["player_dismissed"] == player_name].shape[0]
        average = round(runs / dismissals, 2) if dismissals > 0 else runs
        strike_rate = round((runs / deliveries_faced) * 100, 2) if deliveries_faced > 0 else 0
        fours = data[data["batsman_runs"] == 4].shape[0]
        sixes = data[data["batsman_runs"] == 6].shape[0]
        boundaries = fours + sixes
        boundary_percent = round((boundaries / deliveries_faced) * 100, 2) if deliveries_faced > 0 else 0
        ball_boundary_ratio = round(deliveries_faced/boundaries, 2) if boundaries > 0 else 0

        return {
            "innings_played": innings_played,
            "runs": runs,
            "deliveries_faced": deliveries_faced,
            "average": average,
            "strike_rate": strike_rate,
            "fours": fours,
            "sixes": sixes,
            "boundaries": boundaries,
            "boundary_percent": boundary_percent,
            "ball_boundary_ratio": ball_boundary_ratio
        }
    
    def bowling_stats(data):
        legal_deliveries = data[data["isWide"].isna() & data["isNoBall"].isna()]
        balls_bowled = len(legal_deliveries)
        innings_played = data["matchId"].nunique()
        wickets = data[(data["player_dismissed"].notna()) &(~data["dismissal_kind"].isin(["run out", "retired hurt", "obstructing the field"]))].shape[0]
        runs_conceded = data["total_runs"].sum()
        economy = round((runs_conceded / balls_bowled) * 6, 2) if balls_bowled > 0 else 0
        bowling_strike_rate = round(balls_bowled / wickets, 2) if wickets > 0 else 0
        wickets_per_match = round(wickets / innings_played, 2) if innings_played > 0 else 0
        dot_balls = legal_deliveries[legal_deliveries["total_runs"] == 0].shape[0]
        dot_ball_percent = round((dot_balls / balls_bowled) * 100, 2) if balls_bowled > 0 else 0
    
        return {
                "innings_played": innings_played,
                "wickets": wickets,
                "balls_bowled": balls_bowled,
                "economy": economy,
                "bowling_strike_rate": bowling_strike_rate,
                "wickets_per_match": wickets_per_match,
                "dot_ball_percent": dot_ball_percent
            }


    potm_count = matches[matches["player_of_match"] == player_name].shape[0]
   
    return {
        "player_name": player_name,
        "potm": potm_count,
        "batting": {
            "alltime": batting_stats(batter_data),
            "recent": batting_stats(recent_batter_data)
        },
        "bowling": {
            "alltime": bowling_stats(bowler_data),
            "recent": bowling_stats(recent_bowler_data)
        }
    }
