import streamlit as st

# Setting up the page config
st.set_page_config(page_icon="🛒", page_title="Retail Order Data Analysis", layout="wide")

st.title(''':orange[Welcome to Retail Order Data Analysis]''')

# Home page content
st.page_link("Menu.py", label="Home", icon="🏠")

# Content for page_1.py
st.page_link("pages/Detailed.py", label="Detailed", icon="1️⃣")

# Content for page_2.py
st.page_link("pages/Insights.py", label="Insights", icon="2️⃣")

#Google Search
st.page_link("http://www.google.com", label="Google", icon="🌎")