# Streamlit Playground
This repository contains code for a Streamlit app that demonstrates the usage of various Streamlit features and functionalities.
## Installation
To install the app, first clone this repository to your local machine:

```
git clone https://github.com/chatgpt/streamlit-playground.git
```

Then, navigate to the repository's root directory and run the following command to install the required dependencies:

```
pip install streamlit
```
## Usage
To launch the app, navigate to the repository's root directory and run the following command:

```
streamlit run streamlit_app.py
```

This will launch a Streamlit app on your local machine that you can interact with.
## Features
The app demonstrates the usage of the following Streamlit features:

### main Page
- Setting page configuration
- Using various text elements, including titles, headers, subheaders, and paragraphs
- Displaying markdown text
- Displaying LaTeX equations
- Displaying code snippets
- Displaying metrics
- Displaying tables and dataframes
- Displaying images, audio files, and videos
- Using interactive widgets, including checkboxes, radio buttons, select boxes, multiselect boxes, buttons, sliders, progress bars, text inputs, text areas, date inputs, and time inputs
- Uploading and displaying files, including images and videos
- Using forms to collect user input
- Using the sidebar to switch between different plot types and displaying the plots using Plotly

### Image scraper
This is a Streamlit app that allows users to search for images on Unsplash by keyword using web scraping. The app uses the BeautifulSoup and Requests libraries to scrape the images from the Unsplash website and display them in a responsive layout using Streamlit columns. The app also provides a download button for each image that opens the image in a new tab for the user to download.

### Image editor
This is a Streamlit app that allows users to upload an image, resize it, rotate it, and apply various filters to it. The app uses the urllib and PIL libraries to download and manipulate the image, and the Streamlit library to create a user interface for the app. The app displays the uploaded image along with its size, mode, and format, and provides sliders and dropdowns for resizing, rotating, and filtering the image. The app is intended to demonstrate the usage of various Streamlit widgets and image manipulation functions.

### Audio to text
This Streamlit app is an audio-to-text converter that allows users to upload an audio file in WAV or MP3 format and converts it to text. The app uses the PyDub and SpeechRecognition libraries to split the audio file into chunks based on silence, and then convert each chunk to text using the Google speech-to-text API. The app displays the uploaded audio file and the recognized text, and provides a download button for the user to download the converted text as a text file. The app is intended to demonstrate the usage of various Streamlit widgets and audio-to-text conversion functions.



## Credits
This app was created by Streamlit documentation and tutorials. The app is intended to serve as a reference for Streamlit beginners and to demonstrate the various features and functionalities of Streamlit. If you have any questions or feedback, please feel free to reach out.
