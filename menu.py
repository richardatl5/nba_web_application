import streamlit as st
from multiapp import MultiApp
from apps import home, stats

app = MultiApp()

st.markdown("""
This application is powered by Streamlit, Pandas, Sklearn, & Tableau
""")

app.add_app("Home", home.app)
app.add_app("Stats", stats.app)
# app.add_app("About Me", about.app)

app.run()