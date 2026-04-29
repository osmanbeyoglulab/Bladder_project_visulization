import streamlit as st
from style import page_style, footer
import pandas as pd
from style import define_layout
import os
# st.cache_data.clear()
# st.cache_resource.clear()


# --- PAGE SETUP ----

st.set_page_config(
        page_title='Data Visulization',
        initial_sidebar_state="expanded",
        # layout="wide" 
)

# max_width_str = f"max-width: {80}%;"

# st.markdown(f"""
#         <style>
#         .appview-container .main .block-container{{{max_width_str}}}
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

define_layout(max_width='80%', padding_top='2rem', padding_right='0rem', padding_left='0rem', padding_bottom='0rem')

# Get the directory where the script is located

@st.cache_data
def get_feature_names(directory):
    feature_names = []
    for filename in os.listdir(directory):
        if filename.endswith("_spatial.png"):
            feature_names.append(filename.split("_spatial")[0])

    return feature_names

if "marker_names" not in st.session_state:
    data_path = "./feature_spatial_plots/marker_spatial_plots_1x8_noTitle_scaled"   # <-- update this path
    st.session_state["marker_names"] = get_feature_names(data_path)

if "tf_names" not in st.session_state:
    data_path = "./feature_spatial_plots/tf_spatial_plots_1x8_noTitle_scaled"   # <-- update this path
    st.session_state["tf_names"] = get_feature_names(data_path)



    
# ---- start main ---

emoji = "🔹" #"🔸" #"💠" #"🔹" # # #
feature_page = st.Page(
    page = "feature_spatial.py",
    title = "Feature_spatial",
    icon = emoji,   #":material/chevron_right:"  ,
    default= True,
)

quality_page = st.Page(
    page = "quality_check.py",
    title = "Quality_check",
    icon = emoji
)


# -- NAVIGATION --



pg = st.navigation(
    {
       "": [feature_page, quality_page],
    }
)

pg.run()
