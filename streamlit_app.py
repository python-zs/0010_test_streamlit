# ```pip install streamlit```
""" streamlit playground """

import time as t
from datetime import time
import streamlit as st
import pandas as pd
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

# set page config
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# ```streamlit run .\main.py```

st.title("第一個streamlit Playground")
st.header("good Header")
st.subheader("good subheader")
st.text("paragraph")

# markdown usage
st.title("markdown usage")
st.markdown("---")
st.markdown("## good markdown [link](https://www.google.com)")
st.markdown("* list  \n \
> quote")
st.markdown("```import streamlit as st```")

# latex usage
st.title("latex usage")
st.latex(r'''e^{i\pi} + 1 = 0''') # [katex]https://katex.org/docs/supported.html
st.latex(r'''\begin{CD}
   A @>a>> B \\
@VbVV @AAcA \\
   C @= D
\end{CD}''')

# code usage
st.title("code usage")
json = {"name": "streamlit", "version": "0.65.2"}
st.json(json)
CODE = '''
def hello():
    print("hello world")
'''
st.code(CODE, language="python")

# metrics usage
st.title("metrics usage")
st.metric("Windspeed", "120ms-1", "-1.4ms-1")

# table usage
st.title("table/dataframe usage")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.table(df)
st.dataframe(df)

# image usage
st.title("image usage")

st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png",
          width=300, caption="streamlit logo")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.video("https://www.youtube.com/watch?v=9bZkp7q19f0")

# hide menu and footer
st.markdown('''<style>
# MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>''', unsafe_allow_html=True)

# interactive widgets
st.title("interactive widgets")

def change():
    """change function for checkbox"""
    # basic print
    print("checkbox changed")
    # print session state
    print(st.session_state.chacker)
# checkbox wtih session state and change function
checkbox = st.checkbox("Show/hide",value=True, on_change=change,key="chacker")

# radio button with session state
radio_btn = st.radio("radio button", ["option1", "option2", "option3"])

# selectbox
selectbox = st.selectbox("selectbox", ["option1", "option2", "option3"])

#multiselect
multiselect = st.multiselect("multiselect", ["option1", "option2", "option3"])

# button
def btn_click():
    """button click function"""
    print(f'checkbox={checkbox}')
    print(f'radio_btn={radio_btn}')
    print(f'selectbox={selectbox}')
    print(f'multiselect={multiselect}')
btn = st.button("button", on_click=btn_click)

# File uploader
st.title("File uploader")
# uploaded_file = st.file_uploader("Choose a file", type="csv")
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.write(df)
uploaded_file = st.file_uploader("Choose a file",
                                 type=["png", "jpg", "jpeg","mp4"],
                                 accept_multiple_files=True)
if uploaded_file is not None:
    for file in uploaded_file:
        if file.type == "image/png" or file.type == "image/jpg" or file.type == "image/jpeg":
            image = Image.open(file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)
        elif file.type == "video/mp4":
            st.video(file)

# slider
st.title("slider")
slider = st.slider("slider", min_value=0, max_value=100, value=50, step=1)

# progress bar
st.title("progress bar")
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(slider + 1)
    t.sleep(0.1)

# text input
st.title("text input")
text_input = st.text_input("text input", "default value", max_chars=10)

# text area
st.title("text area")
text_area = st.text_area("text area", "default value", height=100)

# date input
st.title("date input")
date_input = st.date_input("date input", value=None, min_value=None, max_value=None, key=None)

# time input
st.title("time input")
time_input = st.time_input("time input", value=time(0,0,0), key="time_input_changed")
# make progress bar sleep as time input
my_bar = st.progress(0)
# Set initial sleep time
SLEEPTIME = 999
# Set initial Progress value display
progress_value = st.empty()
for p in range(100):
    my_bar.progress(p + 1)
    # Check if time_input has been updated
    if st.session_state.time_input_changed:
        # If time_input has been updated, update the sleep time
        time_input = st.session_state.time_input_changed
        SLEEPTIME = (time_input.hour *60 + time_input.minute)/1440
        progress_value.write(f'{p + 1 }%')
    t.sleep(SLEEPTIME)

# Form usage
st.title("Form usage")
st.markdown("<h2 style='text-align: Center;'>User Registration</h2>", unsafe_allow_html=True)
form = st.form("Form 1")
form.text_input("Name")
form.form_submit_button("Submit")
with st.form("Form 2", clear_on_submit=True): # But we wany to keep filled data when wrong submit
    col1,col2 = st.columns(2)
    firstName = col1.text_input("Name2")
    lastName = col2.text_input("lastName2")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day,month,year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state = st.form_submit_button("Submit2")
    if s_state:
        if firstName == "" or lastName == "":
            st.error("Please fill in all fields")
        else:
            st.success("Form submitted successfully")

# Sidebar & Plotly usage
st.title("Sidebar & Plotly usage")
sidebar = st.sidebar.radio("Sidebar, please select", options=["Line", "Bar", "BarH"])
x = np.linspace(0, 10, 100)
x_bar = np.array([1,2,3,4,5])
fig = plt.figure()
plt.style.use(
    "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
if sidebar == "Line":
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x),"--")
if sidebar == "Bar":
    plt.bar(x_bar, x_bar*10)
if sidebar == "BarH":
    plt.barh(x_bar, x_bar*10)
st.write(fig)
