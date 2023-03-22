"""Web Scraper using Streamlit"""
from bs4 import BeautifulSoup
import requests
import streamlit as st

# Web Scraper
st.title("Web Scraper")
with st.form("Search"):
    keyword = st.text_input("Keyword", "plant")
    search = st.form_submit_button("Search")
    col1, col2, col3 = st.columns(3)
if search:
    # (1) get images from unsplash by keyword using requests and beautifulsoup
    url = f"https://unsplash.com/s/photos/{keyword}"
    page = requests.get(url, timeout=10)
    soup = BeautifulSoup(page.content, 'html.parser')
    images = soup.select("body figure>div>div>div>div>a img")
    height = len(images)
    # (2) st.write(images) into 3 columns according to height
    for index,image in enumerate(images):
        if index < int(height/3):
            col1.image(image['src'])
            # add download button which open new tab
            col1.markdown(f'<a href="{image["src"]}" target="_blank">Download</a>',
                        unsafe_allow_html=True)
        elif index < int(height*2/3):
            col2.image(image['src'])
        else:
            col3.image(image['src'])
