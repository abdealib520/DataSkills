# [DataSkills](https://abdealib520-dataskills-main-i93jq5.streamlit.app/)
This is a website that i created that will tell you what kind of skills are required in the Data Science industry based on data taken from real world jobs. The jobs that were used were all based in India.
The website was built using the streamlit library.

# Conclusion
1. The skills that were required the most for Data Analyst Roles were SQL, Python, Excel and Tableau. The main emphasis here was on Excel.
2. The skills that were required the most for Data Scientist Roles were SQL, Python, Excel and Tableau. The main emphasis here was on Python
3. The skills that were required the most for Data Engineer Roles were SQL, Python, Excel, Airflow, Snowflake and Redshift. The main emphasis here was on SQL.

## Data Collection
The data was collected from [Jsearch](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch/) API available on RapidAPI. The data was retrieved in a JSON format

## Data Cleaning
1. Converted the data from JSON to a pandas dataframe
2. Created many new boolean columns for storing whether a job required a particular skill.
3. From the Data Analyst dataframe I removed all the jobs which did not contain data analyst in their titles. This was repeated for Data Scientist and Data Engineer as well.

## Exploratory Data Analysis
# Bar Chart for Programming Skills in Data Analyst Roles
![image](https://user-images.githubusercontent.com/132557392/236671725-ffc042bd-5061-4d1a-9077-ba93640f7946.png)

# Bar Chart for Software Skills in Data Analyst Roles
![image](https://user-images.githubusercontent.com/132557392/236671733-55a9b467-3a11-4f1e-af6d-f4955a9fbd53.png)

# Bar Chart for Programming Skills in Data Scientist Roles
![image](https://user-images.githubusercontent.com/132557392/236671746-b1178e33-7630-4e33-847a-cf9ca5335e03.png)

# Bar Chart for Software Skills in Data Scientist Roles
![image](https://user-images.githubusercontent.com/132557392/236671752-b6e57233-eaed-480d-a3fd-02a33fb69841.png)

# Bar Chart for Programming Skills in Data Engineer Roles
![image](https://user-images.githubusercontent.com/132557392/236671762-a9412579-0021-42f1-9823-605019f8e4f2.png)

# Bar Chart for Software Skills in Data Engineer Roles
![image](https://user-images.githubusercontent.com/132557392/236671775-36b94713-307c-4c15-befa-d3c451bf19ce.png)
