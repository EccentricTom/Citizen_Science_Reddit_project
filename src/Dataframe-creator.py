# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:29:28 2020

@author: tom
"""
# Load the two packages necessary

import streamlit as st
import pandas as pd

st.title('Data from queried Subreddit')

df = pd.read_csv(r"C:\Users\tom\OneDrive\Documents\Propulsion\Work\group_projects\reddit-api-scraping\data\observation_data.csv", index_col= "Title")

st.write(df.to_html(escape=False), unsafe_allow_html = True)
