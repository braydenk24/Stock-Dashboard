import streamlit as st
from streamlit.components.v1 import html
import main_page
import alert_page

# Define function to render main page
def render_main_page():
    main_page.run()

# Define function to render alert page
def render_alert_page():
    alert_page.run()

# Define the Streamlit app layout
def app():
    st.set_page_config(page_title='My Streamlit App')
    st.title('My Streamlit App')
    menu = ['Main Page', 'Alert Page']
    choice = st.sidebar.selectbox('Select Page', menu)

    # Render main page or alert page based on user's choice
    if choice == 'Main Page':
        render_main_page()
    elif choice == 'Alert Page':
        render_alert_page()

if __name__ == '__main__':
    app()
