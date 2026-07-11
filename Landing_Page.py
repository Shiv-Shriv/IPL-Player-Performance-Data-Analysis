import streamlit as st

st.set_page_config(page_title = "IPL Player Analysis Engine", layout="wide")
st.title("Welcome to the IPL Player Analysis Engine!", text_alignment="center")


st.text("\n")

st.markdown("""
### The Player Analysis Engine allows you to:
""", text_alignment="center")
st.divider()
col1, col2 = st.columns(2)

st.text("\n")

with col1:
    with st.container(border=True, width=1000):
        st.subheader("Player Statistical Analysis")
        st.write("View detailed all-time and recent statistical performance of every player in the Indian Premier League")
        if st.button("Launch →", key="statistics"):
            st.switch_page("pages/Player_Statistical_Analysis.py")

            st.divider()

    with st.container(border=True, width=1000):
        st.subheader("Player Impact Score")
        st.write("View the overall impact score of every IPL player based on a custom metric that combines multiple batting and bowling statistics into a single performance score.")
        if st.button("Launch →", key="impact"):
            st.switch_page("pages/Player_Impact_Score.py")

    

with col2:
     with st.container(border=True, width=1000):
        st.subheader("Player Comparison Analysis")
        st.write("View and compare detailed all-time and recent statistical performance of any two players in the Indian Premier League.")
        if st.button("Launch →", key="comparison"):
            st.switch_page("pages/Player_Comparison.py")

     with st.container(border=True, width=1000):
        st.subheader("Player Reliability Index")
        st.write("View the reliability index of every IPL player based on a custom metric that measures the consistency of their batting and bowling performances over time.")
        if st.button("Launch →", key="reliability"):
            st.switch_page("pages/Player_Reliability_Index.py")

st.divider()


st.subheader("Project Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("IPL Seasons Covered", "2008–2025")

with col2:
    st.metric("Matches Analyzed", "1,095")

with col3:
    st.metric("Deliveries Processed", "261,382")

with col4:
    st.metric("Players Analyzed", "672")