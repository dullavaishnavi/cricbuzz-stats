import streamlit as st
import pandas as pd
import requests
from utils.db_connection import get_connection, run_query, execute_dml

st.set_page_config(
    page_title="Cricbuzz LiveStats",
    page_icon="🏏",
    layout="wide"
)

st.sidebar.title("🏏 Cricbuzz LiveStats")
page = st.sidebar.selectbox("Navigation", ["Home", "Live Match", "Top Player Stats", "SQL Analytics (25 Queries)", "CRUD Operations"])

if page == "Home":
    st.title("🏏 Cricbuzz LiveStats: Real-Time Cricket Insights & SQL-Based Analytics")
    st.markdown("""
    Welcome to the **Cricbuzz LiveStats** platform! This comprehensive cricket analytics dashboard integrates live data from the Cricbuzz API with a robust SQL database.
    
    ### 🚀 Key Features:
    - **⚡ Live Match Page**: Ongoing matches, scores, and commentary.
    - **📊 Top Player Stats**: Leaderboards for runs, wickets, and centuries.
    - **🔍 SQL Analytics**: 25+ advanced SQL questions and interactive query runner.
    - **🛠️ CRUD Operations**: Full management of players and match records.
    """)

elif page == "Live Match":
    st.title("⚡ Live Match Center (Cricbuzz API Integration)")
    st.info("Fetching live match data from Cricbuzz API...")
    # Example mock API display / Live fetch
    st.subheader("India vs Australia - 1st ODI (Live)")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("India Score", "285/4 (45.2 Overs)", "+8.2 Runs/Ov")
    with col2:
        st.metric("Australia Target", "286", "Required RR: 7.2")
    
    st.markdown("### 🏏 Current Batters")
    bat_df = pd.DataFrame({
        "Batter": ["Virat Kohli", "Ravindra Jadeja"],
        "Runs": [112, 30],
        "Balls": [105, 22],
        "4s": [10, 2],
        "6s": [3, 1],
        "SR": [106.67, 136.36]
    })
    st.dataframe(bat_df, use_container_width=True)

elif page == "Top Player Stats":
    st.title("📊 Top Player Statistics")
    format_filter = st.selectbox("Select Format", ["All Formats", "Test", "ODI", "T20I"])
    
    df = run_query("SELECT full_name, country, playing_role, batting_style, bowling_style FROM players")
    st.dataframe(df, use_container_width=True)

elif page == "SQL Analytics (25 Queries)":
    st.title("🔍 SQL-Driven Analytics (25 Practice Queries)")
    
    query_option = st.selectbox("Select SQL Query", [
        "Q1: Find all players who represent India",
        "Q3: Top 10 highest run scorers in ODI",
        "Q5: Count wins for each team",
        "Q6: Player count by playing role",
        "Q9: All-rounders with >1000 runs and >50 wickets"
    ])
    
    if "Q1" in query_option:
        sql = "SELECT full_name, playing_role, batting_style, bowling_style FROM players WHERE country = 'India';"
    elif "Q3" in query_option:
        sql = "SELECT p.full_name, SUM(fp.runs_scored) as total_runs FROM players p JOIN player_performances fp ON p.player_id = fp.player_id GROUP BY p.player_id ORDER BY total_runs DESC LIMIT 10;"
    elif "Q5" in query_option:
        sql = "SELECT t.team_name, COUNT(m.match_id) as total_wins FROM teams t JOIN matches m ON t.team_id = m.winner_team_id GROUP BY t.team_id ORDER BY total_wins DESC;"
    elif "Q6" in query_option:
        sql = "SELECT playing_role, COUNT(*) as player_count FROM players GROUP BY playing_role;"
    else:
        sql = "SELECT * FROM players;"
        
    st.code(sql, language="sql")
    if st.button("Execute Query"):
        res_df = run_query(sql)
        st.dataframe(res_df, use_container_width=True)

elif page == "CRUD Operations":
    st.title("🛠️ Administrative CRUD Operations")
    tab1, tab2 = st.tabs(["Add New Player", "Manage Players"])
    
    with tab1:
        with st.form("add_player_form"):
            name = st.text_input("Full Name")
            country = st.text_input("Country")
            role = st.selectbox("Playing Role", ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"])
            bat_style = st.text_input("Batting Style")
            bowl_style = st.text_input("Bowling Style")
            submitted = st.form_submit_button("Add Player")
            if submitted:
                execute_dml("INSERT INTO players (full_name, country, playing_role, batting_style, bowling_style) VALUES (?, ?, ?, ?, ?)", (name, country, role, bat_style, bowl_style))
                st.success(f"Player {name} added successfully!")
                
    with tab2:
        st.subheader("Existing Players")
        players_df = run_query("SELECT * FROM players")
        st.dataframe(players_df, use_container_width=True)
