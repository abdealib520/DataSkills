import streamlit as st
from logic import DataAnalyst,DataScientist,DataEngineer

data_analyst = DataAnalyst()
data_scientist = DataScientist()
data_engineer = DataEngineer()

st.set_page_config(page_title='Data Skills',layout='wide')

selection = st.sidebar.selectbox(
    "Select your Job",
    ("Data Analyst", "Data Scientist", "Data Engineer")
)
st.title(selection + ' Job Requirements')

if selection == 'Data Analyst':
    col1,col2 = st.columns(2)
    with col1:
        col1.subheader("Programming Languages")
        a = data_analyst.programming()
        st.pyplot(a)
    with col2:
        col2.subheader("Software")
        a = data_analyst.software()
        st.pyplot(a)
    st.markdown('---')
    col1,col2 = st.columns(2)
    with col1:
        count = data_analyst.count()
        st.metric(label='Number of Jobs Searched',value=count)
    with col2:
        col2.subheader("Cities Where The Jobs Are From")
        a = data_analyst.cities()
        st.pyplot(a)
elif selection == 'Data Scientist':
    col1,col2 = st.columns(2)
    with col1:
        col1.subheader("Programming Languages")
        a = data_scientist.programming()
        st.pyplot(a)
    with col2:
        col2.subheader("Software")
        a = data_scientist.software()
        st.pyplot(a)
    st.markdown('---')
    col1,col2 = st.columns(2)
    with col1:
        count = data_scientist.count()
        st.metric(label='Number of Jobs Searched',value=count)
    with col2:
        col2.subheader("Cities Where The Jobs Are From")
        a = data_scientist.cities()
        st.pyplot(a)
elif selection == 'Data Engineer':
    col1,col2 = st.columns(2)
    with col1:
        col1.subheader("Programming Languages")
        a = data_engineer.programming()
        st.pyplot(a)
    with col2:
        col2.subheader("Software")
        a = data_engineer.software()
        st.pyplot(a)
    st.markdown('---')
    col1,col2 = st.columns(2)
    with col1:
        count = data_engineer.count()
        st.metric(label='Number of Jobs Searched',value=count)
    with col2:
        col2.subheader("Cities Where The Jobs Are From")
        a = data_engineer.cities()
        st.pyplot(a)

