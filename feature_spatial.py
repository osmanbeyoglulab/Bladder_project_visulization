import streamlit as st
import base64
from pathlib import Path

st.markdown("<h2 style='text-align: center; color: black;'>Feature spatial</h1>", unsafe_allow_html=True)  
st.write("")


tf_names = st.session_state.get("tf_names", [])
marker_names = st.session_state.get("marker_names", [])


tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

imgfile = f"./feature_spatial_plots/HE_images_1x8/HE_1x8.png"
img_b64 = base64.b64encode(Path(imgfile).read_bytes()).decode()
st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_b64}" style="max-width: 100%; width: 1600px;">
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

option_tf = st.selectbox(
    label='tf',
    options=tf_names,
    ) 

imgfile = f"./feature_spatial_plots/tf_spatial_plots_1x8_noTitle_scaled/{option_tf}_spatial.png"

img_b64 = base64.b64encode(Path(imgfile).read_bytes()).decode()
st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_b64}" style="max-width: 100%; width: 1600px;">
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")


option_marker = st.selectbox(
    label='Marker',
    options=marker_names,
    ) 

imgfile = f"./feature_spatial_plots/marker_spatial_plots_1x8_noTitle_scaled/{option_marker}_spatial.png"

img_b64 = base64.b64encode(Path(imgfile).read_bytes()).decode()
st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_b64}" style="max-width: 100%; width: 1600px;">
    </div>
""", unsafe_allow_html=True)
