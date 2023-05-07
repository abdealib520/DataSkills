import streamlit as st
from logic import DataAnalyst, DataScientist, DataEngineer

data_analyst = DataAnalyst()
data_scientist = DataScientist()
data_engineer = DataEngineer()

st.set_page_config(page_title='Data Skills', layout='wide')

selection = st.sidebar.selectbox(
    "Select your Job",
    ("Data Analyst", "Data Scientist", "Data Engineer")
)
st.title(selection + ' Job Requirements')

if selection == 'Data Analyst':
    col1, col2 = st.columns(2)
    with col1:
        col1.subheader("Programming Languages")
        barchart = data_analyst.programming()
        st.pyplot(barchart)
    with col2:
        col2.subheader("Software")
        barchart = data_analyst.software()
        st.pyplot(barchart)
    st.markdown('---')
    col1, col2 = st.columns(2)
    with col1:
        count = data_analyst.count()
        st.metric(label='Number of Jobs Searched', value=count)
    with col2:
        col2.subheader("Cities Where The Jobs Are From")
        piechart = data_analyst.cities()
        st.pyplot(piechart)
elif selection == 'Data Scientist':
    col1, col2 = st.columns(2)
    with col1:
        col1.subheader("Programming Languages")
        barchart = data_scientist.programming()
        st.pyplot(barchart)
    with col2:
        col2.subheader("Software")
        barchart = data_scientist.software()
        st.pyplot(barchart)
    st.markdown('---')
    col1, col2 = st.columns(2)
    with col1:
        count = data_scientist.count()
        st.metric(label='Number of Jobs Searched', value=count)
    with col2:
        col2.subheader("Cities Where The Jobs Are From")
        piechart = data_scientist.cities()
        st.pyplot(piechart)
elif selection == 'Data Engineer':
    col1, col2 = st.columns(2)
    with col1:
        col1.subheader("Programming Languages")
        barchart = data_engineer.programming()
        st.pyplot(barchart)
    with col2:
        col2.subheader("Software")
        barchart = data_engineer.software()
        st.pyplot(barchart)
    st.markdown('---')
    col1, col2 = st.columns(2)
    with col1:
        count = data_engineer.count()
        st.metric(label='Number of Jobs Searched', value=count)
    with col2:
        col2.subheader("Cities Where The Jobs Are From")
        piechart = data_engineer.cities()
        st.pyplot(piechart)
