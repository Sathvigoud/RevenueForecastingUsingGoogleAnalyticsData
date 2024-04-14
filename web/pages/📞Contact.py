import streamlit as st

# Page Title with Center Alignment
st.title("Contact Us")

# Create a form
contact_form = st.form("contact")

# Form Fields with Labels and Padding
name = contact_form.text_input(label="Your Name", placeholder="Enter your name")
email = contact_form.text_input(label="Your Email Address", placeholder="Enter your email")
message = contact_form.text_area(label="Your Message", placeholder="Write your message here")

# Submit button with styling
submitted = contact_form.form_submit_button("Send Message")
st.markdown("""<style>
.st-b7 { /* Target the specific class for the button */
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}
</style>""", unsafe_allow_html=True)

if submitted:
    # Implement logic to process the contact form submission here
    # For example, send an email or store the information in a database
    st.success(f"Thanks {name}, your message has been sent!")

# Separator with Line and Padding
#st.write("---")
st.markdown("""<hr style="border-top: 1px solid #ddd; padding: 10px 0px;">""", unsafe_allow_html=True)

# Contact Information with Columns and Styling
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Email")
    st.write("- rashmikannela@gmail.com")
    st.write("- sathvikagoud899@gmail.com")
    st.write("- tabassumsadiya72@gmail.com")
with col2:
    st.subheader("Phone")
    st.write("- +91 9014977845")
    st.write("- +91 9390319506")
    st.write("- +91 8522031088")
with col3:
    # Add an icon for social media (optional)
    # st.write("[Icon Link](icon_url.com)")
    pass

st.markdown(
    """
<style>
 [data-testid="stSidebar"] {
  background-image: linear-gradient(to right, #434343 0%, black 100%);
  }

</style>
""",
    unsafe_allow_html=True
)

