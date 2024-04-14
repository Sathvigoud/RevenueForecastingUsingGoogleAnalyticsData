import streamlit as st
import base64
# Set page title and background image (using CSS)
st.set_page_config(
    page_title="Revenue Prediction",
    #page_config_layout="wide"  # Optional for wider layout
)
@st.cache_data 
def get_img_as_base64(file):
    with open(file,"rb") as f:
        data=f.read()
    return base64.b64encode(data).decode()
img= get_img_as_base64("home.jpeg")

page_bg_img ="""
<style>

[data-testid="stAppViewContainer"]::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("https://www.clari.com/contentassets/ede23a353240407c9582bfdbe04028f7/blog_header2x.png?w=892");
  background-size: cover;  /* Ensure image covers the container */
  z-index: -1;  /* Place behind the actual content */
  filter: blur(5px);  /* Adjust blur level as needed */
}

[data-testid="stAppViewContainer"] {
  /* Maintain original styles for main container */
  background-color: #e5e5f7;
  opacity: 0.8;
  background-repe
}

[data-testid="element-container"]{

}


[data-testid="stHeader"]{
background-color:rgba(0,0,0,0);
}

[data-tesid="stToolbar"]{
right:2rem;
}

[data-testid="stSidebar"]{
background-image :url("data:home/png;base64,{img}");
background-size: cover;
}
[data-testid="stSidebar"] {
  background-image: linear-gradient(to right, #434343 0%, black 100%);
  }
  

</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


# App content
st.sidebar.success("REVENUE FORECASTING USING GOOGLE ANALYTICS DATA")

st.markdown("<div style='position: absolute; top: 0; right: 0;font-size:20px;'>TEAM-32</div>", unsafe_allow_html=True)
st.title("REVENUE FORECASTING USING GOOGLE ANALYTICS DATA")

st.write("___")
#image = st.image("D:/garpm/grapstreamlit/web/revenue.png", width=200) 
st.write("## What We Do")
st.write("The 80/20 rule has proven true for many businesses - only a small percentage of customers produce most of the revenue. As such, marketing teams are challenged to make appropriate investments in promotional strategies. In this project, we analyze a Google Merchandise Store (GStore) customer dataset to predict revenue per customer. This can lead to more actionable operational changes and a better use of marketing budgets for companies using data analysis on top of Google Analytics data.")
