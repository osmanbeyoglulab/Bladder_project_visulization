import streamlit as st
import base64
from pathlib import Path

st.markdown("<h2 style='text-align: center; color: black;'>Data quality check</h1>", unsafe_allow_html=True)  
st.write("")

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

imgfile = f"./data_quality_check/violin_n_genes_by_counts.png"
img_b64 = base64.b64encode(Path(imgfile).read_bytes()).decode()
st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_b64}" style="max-width: 100%; width: 1000px;">
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

imgfile = f"./data_quality_check/violin_total_counts.png"
img_b64 = base64.b64encode(Path(imgfile).read_bytes()).decode()
st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_b64}" style="max-width: 100%; width: 1000px;">
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

imgfile = f"./data_quality_check/violin_pct_counts_mt.png"
img_b64 = base64.b64encode(Path(imgfile).read_bytes()).decode()
st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_b64}" style="max-width: 100%; width: 1000px;">
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
