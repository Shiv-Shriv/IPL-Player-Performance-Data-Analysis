import streamlit as st
import pandas as pd
from core.player_page import get_player_stats
from processing.player_search import contains_player_substring
from core.comparison import higherstatcmp, lowerstatcmp, statcolor

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
            b1 = stats1["batting"]["alltime"]
            b2 = stats2["batting"]["alltime"]

            with left:
                st.markdown(f"## {stats1['player_name']}")
                
                runs_color1 = higherstatcmp(b1["runs"], b2["runs"])
                avg_color1 = higherstatcmp(b1["average"], b2["average"])
                sr_color1 = higherstatcmp(b1["strike_rate"], b2["strike_rate"])
                boundaries_color1 = higherstatcmp(b1["boundaries"], b2["boundaries"])
                bp_color1 = higherstatcmp(b1["boundary_percent"], b2["boundary_percent"])
                bbr_color1 = lowerstatcmp(b1["ball_boundary_ratio"], b2["ball_boundary_ratio"])

                st.markdown(statcolor("Runs", b1["runs"], runs_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Average", b1["average"], avg_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Strike Rate", b1["strike_rate"], sr_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Boundaries", b1["boundaries"], boundaries_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Boundary %", f"{b1['boundary_percent']}%", bp_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Ball/Boundary Ratio", b1["ball_boundary_ratio"], bbr_color1), unsafe_allow_html=True)

            with right:
                st.markdown(f"## {stats2['player_name']}")

                runs_color2 = higherstatcmp(b2["runs"], b1["runs"])
                avg_color2 = higherstatcmp(b2["average"], b1["average"])
                sr_color2 = higherstatcmp(b2["strike_rate"], b1["strike_rate"])
                boundaries_color2 = higherstatcmp(b2["boundaries"], b1["boundaries"])
                bp_color2 = higherstatcmp(b2["boundary_percent"], b1["boundary_percent"])
                bbr_color2 = lowerstatcmp(b2["ball_boundary_ratio"], b1["ball_boundary_ratio"])

                st.markdown(statcolor("Runs", b2["runs"], runs_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Average", b2["average"], avg_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Strike Rate", b2["strike_rate"], sr_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Boundaries", b2["boundaries"], boundaries_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Boundary %", f"{b2['boundary_percent']}%", bp_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Ball/Boundary Ratio", b2["ball_boundary_ratio"], bbr_color2), unsafe_allow_html=True)
        
        with inner_tab2:
            
            left, right = st.columns(2)
            br1 = stats1["batting"]["recent"]
            br2 = stats2["batting"]["recent"]

            with left:
                st.markdown(f"## {stats1['player_name']}")
                
                runs_color1 = higherstatcmp(br1["runs"], br2["runs"])
                avg_color1 = higherstatcmp(br1["average"], br2["average"])
                sr_color1 = higherstatcmp(br1["strike_rate"], br2["strike_rate"])
                boundaries_color1 = higherstatcmp(br1["boundaries"], br2["boundaries"])
                bp_color1 = higherstatcmp(br1["boundary_percent"], br2["boundary_percent"])
                bbr_color1 = lowerstatcmp(br1["ball_boundary_ratio"], br2["ball_boundary_ratio"])

                st.markdown(statcolor("Runs", br1["runs"], runs_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Average", br1["average"], avg_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Strike Rate", br1["strike_rate"], sr_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Boundaries", br1["boundaries"], boundaries_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Boundary %", f"{br1['boundary_percent']}%", bp_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Ball/Boundary Ratio", br1["ball_boundary_ratio"], bbr_color1), unsafe_allow_html=True)

            with right:
                st.markdown(f"## {stats2['player_name']}")
                
                runs_color2 = higherstatcmp(br2["runs"], br1["runs"])
                avg_color2 = higherstatcmp(br2["average"], br1["average"])
                sr_color2 = higherstatcmp(br2["strike_rate"], br1["strike_rate"])
                boundaries_color2 = higherstatcmp(br2["boundaries"], br1["boundaries"])
                bp_color2 = higherstatcmp(br2["boundary_percent"], br1["boundary_percent"])
                bbr_color2 = lowerstatcmp(br2["ball_boundary_ratio"], br1["ball_boundary_ratio"])

                st.markdown(statcolor("Runs", br2["runs"], runs_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Average", br2["average"], avg_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Strike Rate", br2["strike_rate"], sr_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Boundaries", br2["boundaries"], boundaries_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Boundary %", f"{br2['boundary_percent']}%", bp_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Ball/Boundary Ratio", br2["ball_boundary_ratio"], bbr_color2), unsafe_allow_html=True)



    with tab2:
        inner_tab1, inner_tab2 = st.tabs(["All-Time", "Recent(Last 3 Years)"])

        with inner_tab1:
            left, right = st.columns(2)
            bw1 = stats1["bowling"]["alltime"]
            bw2 = stats2["bowling"]["alltime"]

            with left:
                st.markdown(f"## {stats1['player_name']}")

                wickets_color1 = higherstatcmp(bw1["wickets"], bw2["wickets"])
                economy_color1 = lowerstatcmp(bw1["economy"], bw2["economy"])
                bsr_color1 = lowerstatcmp(bw1["bowling_strike_rate"], bw2["bowling_strike_rate"])
                wpm_color1 = higherstatcmp(bw1["wickets_per_match"], bw2["wickets_per_match"])
                dbp_color1 = higherstatcmp(bw1["dot_ball_percent"], bw2["dot_ball_percent"])
                
                st.markdown(statcolor("Wickets", bw1["wickets"], wickets_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Economy", bw1["economy"], economy_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Strike Rate", bw1["bowling_strike_rate"], bsr_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Wickets/Match", bw1["wickets_per_match"], wpm_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Dot Ball %", f"{bw1['dot_ball_percent']}%", dbp_color1), unsafe_allow_html=True)
                

            with right:
                st.markdown(f"## {stats2['player_name']}")
                
                wickets_color2 = higherstatcmp(bw2["wickets"], bw1["wickets"])
                economy_color2 = lowerstatcmp(bw2["economy"], bw1["economy"])
                bsr_color2 = lowerstatcmp(bw2["bowling_strike_rate"], bw1["bowling_strike_rate"])
                wpm_color2 = higherstatcmp(bw2["wickets_per_match"], bw1["wickets_per_match"])
                dbp_color2 = higherstatcmp(bw2["dot_ball_percent"], bw1["dot_ball_percent"])
                
                st.markdown(statcolor("Wickets", bw2["wickets"], wickets_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Economy", bw2["economy"], economy_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Strike Rate", bw2["bowling_strike_rate"], bsr_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Wickets/Match", bw2["wickets_per_match"], wpm_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Dot Ball %", f"{bw2['dot_ball_percent']}%", dbp_color2), unsafe_allow_html=True)

        with inner_tab2:
            left, right = st.columns(2)
            bwr1 = stats1["bowling"]["recent"]
            bwr2 = stats2["bowling"]["recent"]

            with left:
                st.markdown(f"## {stats1['player_name']}")
                
                wickets_color1 = higherstatcmp(bwr1["wickets"], bwr2["wickets"])
                economy_color1 = lowerstatcmp(bwr1["economy"], bwr2["economy"])
                bsr_color1 = lowerstatcmp(bwr1["bowling_strike_rate"], bwr2["bowling_strike_rate"])
                wpm_color1 = higherstatcmp(bwr1["wickets_per_match"], bwr2["wickets_per_match"])
                dbp_color1 = higherstatcmp(bwr1["dot_ball_percent"], bwr2["dot_ball_percent"])
                
                st.markdown(statcolor("Wickets", bwr1["wickets"], wickets_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Economy", bwr1["economy"], economy_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Strike Rate", bwr1["bowling_strike_rate"], bsr_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Wickets/Match", bwr1["wickets_per_match"], wpm_color1), unsafe_allow_html=True)
                st.markdown(statcolor("Dot Ball %", f"{bwr1['dot_ball_percent']}%", dbp_color1), unsafe_allow_html=True)
                

            with right:
                st.markdown(f"## {stats2['player_name']}")
                
                wickets_color2 = higherstatcmp(bwr2["wickets"], bwr1["wickets"])
                economy_color2 = lowerstatcmp(bwr2["economy"], bwr1["economy"])
                bsr_color2 = lowerstatcmp(bwr2["bowling_strike_rate"], bwr1["bowling_strike_rate"])
                wpm_color2 = higherstatcmp(bwr2["wickets_per_match"], bwr1["wickets_per_match"])
                dbp_color2 = higherstatcmp(bwr2["dot_ball_percent"], bwr1["dot_ball_percent"])
                
                st.markdown(statcolor("Wickets", bwr2["wickets"], wickets_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Economy", bwr2["economy"], economy_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Strike Rate", bwr2["bowling_strike_rate"], bsr_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Wickets/Match", bwr2["wickets_per_match"], wpm_color2), unsafe_allow_html=True)
                st.markdown(statcolor("Dot Ball %", f"{bwr2['dot_ball_percent']}%", dbp_color2), unsafe_allow_html=True)