import pandas as pd

matches = pd.read_csv("data/raw/matches_updated_ipl_upto_2025.csv")

deliveries = pd.read_csv("data/raw/deliveries_updated_ipl_upto_2025.csv")

deliveries["total_runs"] = (
    deliveries["batsman_runs"] +
    deliveries["extras"])

import streamlit as st
from core.player_page import get_player_stats

st.set_page_config(page_title="IPL Player Data", layout="wide")

st.title("IPL Player Data")

player_name = st.text_input("Search Player", placeholder="e.g. MS Dhoni, V Kohli")

if player_name:
    stats = get_player_stats(player_name)

    if stats["batting"]["alltime"]["innings_played"] == 0 and stats["bowling"]["alltime"]["innings_played"] == 0:
        st.error(f"No data found for '{player_name}'. Check the spelling.")

    else:
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
                st.metric("Boundary/Ball Ratio", b["boundary_ball_ratio"])

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
                st.metric("Boundary/Ball Ratio", r["boundary_ball_ratio"])

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

