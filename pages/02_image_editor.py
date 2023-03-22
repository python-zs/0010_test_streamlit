""" Image editor """
import urllib.request
from PIL import Image, ImageFilter
import streamlit as st

st.title("Image editor")
# can't use Image.open("https://www.w3schools....") because this error:
# OSError: [Errno 22] Invalid argument: 'https://www.w3schools.com/w3css/img_lights.jpg'

urllib.request.urlretrieve(
  'https://www.w3schools.com/w3css/img_lights.jpg',
   "img_lights.jpg")

img = Image.open("img_lights.jpg")
_size = st.empty()
_mode = st.empty()
_format = st.empty()
if img:
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    _size.write(img.size)
    _mode.write(img.mode)
    _format.write(img.format)
    rezise_slider = st.slider("image_resize_slider",
                              min_value=0, max_value=200, value=50, step=1)
    # resize image by slider value
    new_img = img.resize((rezise_slider, rezise_slider))
    st.image(new_img, caption='resized Image.',
             use_column_width="auto")
    # create slider for image rotation
    rotate_slider = st.slider("image_rotate_slider",
                              min_value=0, max_value=200, value=50, step=1)
    # rotate image by slider value
    rotated_img = new_img.rotate(rotate_slider)
    st.image(rotated_img, caption='rotated Image.',
             use_column_width="auto")
    # create dropdown for image filter
    filter_dropdown = st.selectbox("image_filter_dropdown",
                                   options=["BLUR", "CONTOUR", "DETAIL",
                                             "EDGE_ENHANCE", "EDGE_ENHANCE_MORE",
                                            "EMBOSS", "FIND_EDGES", "SHARPEN",
                                              "SMOOTH", "SMOOTH_MORE"])
    # filter image by dropdown value
    filtered_img = rotated_img.filter(getattr(ImageFilter, filter_dropdown))
    st.image(filtered_img, caption='filtered Image.',
             use_column_width="auto")
