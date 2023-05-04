# [DataSkills](https://abdealib520-dataskills-main-i93jq5.streamlit.app/)
This is a website that i created that will tell you what kind of skills are required in the Data Science industry based on data taken from real world jobs.

## Data Collection
The data was collected from [Jsearch](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch/) API available on RapidAPI. The data was retrieved in a JSON format

## Data Cleaning
1. Converted the data from JSON to a pandas dataframe
2. Created many new boolean columns for storing whether a job required a particular skill.
3. From the Data Analyst dataframe I removed all the jobs which did not contain data analyst in their titles. This was repeated for Data Scientist and Data Engineer as well.
