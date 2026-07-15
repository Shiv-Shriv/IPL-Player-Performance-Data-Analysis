import streamlit as st
import pandas as pd
from core.player_page import get_player_stats
from processing.player_search import contains_player_substring

st.set_page_config(page_title="Player Statistical Analysis", layout="wide")
st.title("Player Statistical Analysis")

player_input = st.text_input("Search Player", placeholder="e.g. MS Dhoni, V Kohli")

player_list = contains_player_substring(player_input)

player_name = None

if(player_input != ""):
    if(len(player_list)==0):
        st.error(f"No data found for '{player_input}'. Check the spelling.")
    elif(player_input==player_list[0]):
        player_name = player_list[0]
    
    else:
        player_list.insert(0, "Select a player..")
        player_name = st.selectbox("Search Suggestions:", player_list)

    
    if((player_name!="Select a player..")and(player_name!=None)):

        stats = get_player_stats(player_name)

        
        st.markdown(f"## {stats['player_name']}")
        st.markdown(f"**Player of the Match Awards:** {stats['potm']}")
        st.divider()

        tab1, tab2 = st.tabs(["Batting", "Bowling"])

        with tab1:
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### All-Time")
                b = stats["batting"]["alltime"]
                st.metric("Innings Played", b["innings_played"])
                st.metric("Runs Scored", int(b["runs"]))
                st.metric("Deliveries Faced", b["deliveries_faced"])
                st.metric("Average", b["average"])
                st.metric("Strike Rate", b["strike_rate"])
                st.metric("4s", b["fours"])
                st.metric("6s", b["sixes"])
                st.metric("Boundaries", b["boundaries"])
                st.metric("Boundary %", f"{b['boundary_percent']}%")
                st.metric("Ball/Boundary Ratio", b["ball_boundary_ratio"])

            with col2:
                st.markdown("### Recent (Last 3 Years)")
                r = stats["batting"]["recent"]
                st.metric("Innings Played", r["innings_played"])
                st.metric("Runs Scored", int(r["runs"]))
                st.metric("Deliveries Faced", r["deliveries_faced"])
                st.metric("Average", r["average"])
                st.metric("Strike Rate", r["strike_rate"])
                st.metric("4s", r["fours"])
                st.metric("6s", r["sixes"])
                st.metric("Boundaries", r["boundaries"])
                st.metric("Boundary %", f"{r['boundary_percent']}%")
                st.metric("Ball/Boundary Ratio", r["ball_boundary_ratio"])

        with tab2:
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### All-Time")
                bw = stats["bowling"]["alltime"]
                st.metric("Innings Played", bw["innings_played"])
                st.metric("Wickets Taken", bw["wickets"])
                st.metric("Deliveries Bowled", bw["balls_bowled"])
                st.metric("Economy", bw["economy"])
                st.metric("Strike Rate", bw["bowling_strike_rate"])
                st.metric("Wickets/Match", bw["wickets_per_match"])
                st.metric("Dot Ball %", f"{bw['dot_ball_percent']}%")

            with col2:
                st.markdown("### Recent (Last 3 Years)")
                rw = stats["bowling"]["recent"]
                st.metric("Innings Played", rw["innings_played"])
                st.metric("Wickets Taken", rw["wickets"])
                st.metric("Deliveries Bowled", rw["balls_bowled"])
                st.metric("Economy", rw["economy"])
                st.metric("Strike Rate", rw["bowling_strike_rate"])
                st.metric("Wickets/Match", rw["wickets_per_match"])
                st.metric("Dot Ball %", f"{rw['dot_ball_percent']}%")



