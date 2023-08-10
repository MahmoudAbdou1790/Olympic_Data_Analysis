import os
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import streamlit as st

Olympic= pd.read_csv("Cleaned_Olympic2.csv")
st.title("Olympic 🥇 ⛳🥅🏋️‍♀️🚴‍♂️ Data Analysis")
st.image('rio-de-janeiro-2016-1177950_1280.jpg', width=500)
st.write("## Introduction")
st.write(""" This is an Olympic Data Analysis project to analyze the modern Olympic Games, including all the Games from Athens 1896 to Rio 2016.t his analysis provides an opportunity to ask questions about how the Olympics have evolved over time, including the participation and performance of women, different nations, and different sports and events """)
st.write("## Content")
st.write(""" The file dataset_olympics2.csv contains 271116 rows and 15 columns. Each row corresponds to an individual athlete competing in an individual Olympic event (athlete-events). 
The columns are:

    1-ID - Unique number for each athlete
    2-Name - Athlete's name
    3-Sex - M or F
    4-Age - Integer
    5-Height - In centimeters
    6-Weight - In kilograms
    7-Team - Team name
    8-NOC - National Olympic Committee 3-letter code
    9-Games - Year and season
    10-Year - Integer
    11-Season - Summer or Winter
    12-City - Host city
    13-Sport - Sport
    14-Event - Event
    15-Medal - Gold, Silver, Bronze, or NA

The file noc_regions.csv contains 230 rows and 3 columns. Each row corresponds to an individual region. The columns are:

    1-NOC (National Olympic Committee 3 letter code)
    2-region
    3-notes
""")
        
st.video('demo.mp4')

st.markdown("<h1 style='text-align: Left; font-size: 25px;'>Questions </h1>",unsafe_allow_html=True)

st.write(" - How many Olympic games had been organized to date?")
st.write(" - In which cities the Olympic games had been organized?")
st.write(" - How many sports are being played in the Olympics?")
st.write(" - How many events had been organized in the Olympics?")
st.write(" - How many athletes participated in the Olympics? ")
st.write(" - How many countries participate in the Olympics?")
st.write(" - Who are the most successful athletes of all time? (Overall)")
st.write(" - Who are the most successful athletes of all time? (Country)")
st.write(" - Over the years how many participating nations are attented Olympics?")
st.write(" - what is ratio Height vs Weight for Winning Medals?")
st.write(" - what is ratio Gender ratio relation w.r.t Height - Weight for Winning Medals?")
 
   




