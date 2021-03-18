import streamlit as st
import pandas as pd
import base64 # handle data download, encode ascii to byte conversion
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json

def app():
    st.title('NBA Player Statistics Explorer')

    st.markdown("""
    This app web scrapes NBA player statistics and displays the data in a dataframe ready for futrther visualization, analysis and machine learning
    * ** Python Libraries: ** Pandas, Streamlit
    * ** Data Sources: ** [nba.com](https://www.nba.com/)
    """)

    st.sidebar.header('User Input Features')
    selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2022))))

    @st.cache  # data is being cached, so once loaded in 2021, it will not conitnously scrape and rebuild the dataframe
    def load_data(year):
        url = "https://www.basketball-reference.com/leagues/NBA_"+ str(year) +"_per_game.html"
        html = pd.read_html(url, header = 0)
        df = html[0]
        df2 = df.dropna(how = 'all')  # dropping null values
        df3 = df2.fillna(0)    #filling nul values with 0
        df4 = df3.drop(["Rk"], axis =1)   # dropping the index from the orignial table, index was called Rk
        data = df4.drop(df4[df4["Pos"] == "Pos"].index)    #dropping the repeating row (same row)

        return data

    stats = load_data(selected_year)

    st.write("NBA player statistics ranging from 1950 - 2021")


    selected = st.text_input("", "Search...")

    if st.button("Enter"):
        select_df = stats[stats.Player == selected]
        st.write(select_df)


    #selected team 
    unique_teams = sorted(stats.Tm.unique()) # unique items from column Tm (Team). Sorted() arranges it descending (alphabetically)
    selected_team = st.sidebar.multiselect("Team", unique_teams, unique_teams)  # listing it out to traverse 


    #selected pos
    unique_positions = ['C', 'PF', 'SF', 'SG', 'PG']
    selected_position = st.sidebar.multiselect("Position", unique_positions, unique_positions) 


    filtered_selection = stats[(stats.Tm.isin(selected_team)) & (stats.Pos.isin(selected_position))]
    st.write(filtered_selection)







