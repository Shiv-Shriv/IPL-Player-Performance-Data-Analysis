import streamlit as st
import pandas as pd
from core.player_page import get_player_stats
from processing.player_search import contains_player_substring

st.set_page_config(page_title="Player Statistical Analysis", layout="wide")
st.title("Player Statistical Analysis")

stats1 = None
stats2 = None

st.divider()

col1, col2 = st.columns(2)

with col1:
    player_input1 = st.text_input("Search First Player", placeholder="e.g. MS Dhoni, V Kohli")

    player_list1 = contains_player_substring(player_input1)

    player_name1 = None

    if(player_input1 != ""):
        if(len(player_list1)==0):
            st.error(f"No data found for '{player_input1}'. Check the spelling.")
        elif(player_input1==player_list1[0]):
            player_name1 = player_list1[0]
        
        else:
            player_list1.insert(0, "Select a player..")
            player_name1 = st.selectbox("Search Suggestions:", player_list1)

        if ((player_name1!="Select a player..")and(player_name1!=None)):

            stats1 = get_player_stats(player_name1)

with col2:
    player_input2 = st.text_input("Search Second Player", placeholder="e.g. MS Dhoni, V Kohli")

    player_list2 = contains_player_substring(player_input2)

    player_name2 = None

    if(player_input2 != ""):
        if(len(player_list2)==0):
            st.error(f"No data found for '{player_input2}'. Check the spelling.")
        elif(player_input2==player_list2[0]):
            player_name2 = player_list2[0]
        
        else:
            player_list2.insert(0, "Select a player..")
            player_name2 = st.selectbox("Search Suggestions:", player_list2)

        if ((player_name2!="Select a player..")and(player_name2!=None)):

            stats2 = get_player_stats(player_name2)




if ((stats1!=None)and(stats2!=None)):

    st.divider()
    tab1, tab2 = st.tabs(["Batting", "Bowling"])


    with tab1:

        inner_tab1, inner_tab2 = st.tabs(["All-Time", "Recent(Last 3 Years)"])
        with inner_tab1:

            left, right = st.columns(2)

            with left:
                st.markdown(f"## {stats1['player_name']}")
                b1 = stats1["batting"]["alltime"]
                st.metric("Runs", b1["runs"])
                st.metric("Average", b1["average"])
                st.metric("Strike Rate", b1["strike_rate"])
                st.metric("Boundaries", b1["boundaries"])
                st.metric("Boundary %", f"{b1['boundary_percent']}%")
                st.metric("Boundary/Ball Ratio", b1["ball_boundary_ratio"])

            with right:
                st.markdown(f"## {stats2['player_name']}")
                b2 = stats2["batting"]["alltime"]
                st.metric("Runs", b2["runs"])
                st.metric("Average", b2["average"])
                st.metric("Strike Rate", b2["strike_rate"])
                st.metric("Boundaries", b2["boundaries"])
                st.metric("Boundary %", f"{b2['boundary_percent']}%")
                st.metric("Boundary/Ball Ratio", b2["ball_boundary_ratio"])
        
        with inner_tab2:
            
            left, right = st.columns(2)

            with left:
                st.markdown(f"## {stats1['player_name']}")
                br1 = stats1["batting"]["recent"]
                st.metric("Runs", br1["runs"])
                st.metric("Average", br1["average"])
                st.metric("Strike Rate", br1["strike_rate"])
                st.metric("Boundaries", br1["boundaries"])
                st.metric("Boundary %", f"{br1['boundary_percent']}%")
                st.metric("Boundary/Ball Ratio", br1["ball_boundary_ratio"])

            with right:
                st.markdown(f"## {stats2['player_name']}")
                br2 = stats2["batting"]["recent"]
                st.metric("Runs", br2["runs"])
                st.metric("Average", br2["average"])
                st.metric("Strike Rate", br2["strike_rate"])
                st.metric("Boundaries", br2["boundaries"])
                st.metric("Boundary %", f"{br2['boundary_percent']}%")
                st.metric("Boundary/Ball Ratio", br2["ball_boundary_ratio"])



    with tab2:
        inner_tab1, inner_tab2 = st.tabs(["All-Time", "Recent(Last 3 Years)"])

        with inner_tab1:
            left, right = st.columns(2)

            with left:
                st.markdown(f"## {stats1['player_name']}")
                bw1 = stats1["bowling"]["alltime"]
                st.metric("Wickets Taken", bw1["wickets"])
                st.metric("Economy", bw1["economy"])
                st.metric("Strike Rate", bw1["bowling_strike_rate"])
                st.metric("Wickets/Match", bw1["wickets_per_match"])
                st.metric("Dot Ball %", f"{bw1['dot_ball_percent']}%")
                

            with right:
                st.markdown(f"## {stats2['player_name']}")
                bw2 = stats2["bowling"]["alltime"]
                st.metric("Wickets Taken", bw2["wickets"])
                st.metric("Economy", bw2["economy"])
                st.metric("Strike Rate", bw2["bowling_strike_rate"])
                st.metric("Wickets/Match", bw2["wickets_per_match"])
                st.metric("Dot Ball %", f"{bw2['dot_ball_percent']}%")

        with inner_tab2:
            left, right = st.columns(2)

            with left:
                st.markdown(f"## {stats1['player_name']}")
                bwr1 = stats1["bowling"]["recent"]
                st.metric("Wickets Taken", bwr1["wickets"])
                st.metric("Economy", bwr1["economy"])
                st.metric("Strike Rate", bwr1["bowling_strike_rate"])
                st.metric("Wickets/Match", bwr1["wickets_per_match"])
                st.metric("Dot Ball %", f"{bwr1['dot_ball_percent']}%")
                

            with right:
                st.markdown(f"## {stats2['player_name']}")
                bwr2 = stats2["bowling"]["recent"]
                st.metric("Wickets Taken", bwr2["wickets"])
                st.metric("Economy", bwr2["economy"])
                st.metric("Strike Rate", bwr2["bowling_strike_rate"])
                st.metric("Wickets/Match", bwr2["wickets_per_match"])
                st.metric("Dot Ball %", f"{bwr2['dot_ball_percent']}%")