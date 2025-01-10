import streamlit as st

# Setting up the page config
st.set_page_config(page_icon="🛒", page_title="Retail Order Data Analysis", layout="wide")

st.title('''Welcome to Retail Order Data Analysis''')

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://thestatisticsassignmenthelp.com/uploads/services/2024-04-16-12-05-10kupq0tcl74.png");
background-size: cover;
}

</style>
"""

# Display the background image
st.markdown(page_bg_img, unsafe_allow_html=True)

# Home page content
st.page_link("Menu.py", label="Home", icon="🏠")

# Content for page_1.py
st.page_link("pages/Detailed.py", label="Detailed", icon="1️⃣")

# Content for page_2.py
st.page_link("pages/Insights.py", label="Insights", icon="2️⃣")

#Google Search
st.page_link("http://www.google.com", label="Google", icon="🌎")
