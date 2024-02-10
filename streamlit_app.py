import streamlit as st


# st.title("🦋Hi, I'm Nunzia!")
# st.write("")
# st.info("Data Science & Machine Learning || University of Fisciano, Italy || Web Developer Freelancer", icon="💻")


# PROFILE
col1, col2 = st.columns(2)
with col1:
    st.header("Hey there.\n I'm Annunziata Elefante!")
    st.write("I'm a programmer with a specialization in Data Science and Machine Learning.")
    # st.write("Hi there 👋 My name is Annunziata Elefante, but my friends call me :black[Nunzia]. \n I'm a 25-year-old programmer with a specialization in Data Science and Machine Learning. \n\n")
with col2:
    st.image('images/profile.JPG', caption='Annunziata Elefante')    

# SIDEBAR
with st.sidebar:
    # st.image('images/profile.JPG', caption='Nunzia')
    st.write("☰ MENU")
    st.page_link("streamlit_app.py", label="Home", icon="🏡")
    st.page_link("pages/echoBot.py", label="Echo Chat", icon="🤖")

# draw celebratory balloons.
# st.balloons()
