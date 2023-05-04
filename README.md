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
![image](https://user-images.githubusercontent.com/132557392/236205437-ec3cda57-390f-4133-a72d-6884ba9f97e7.png)

# Bar Chart for Software Skills in Data Analyst Roles
![image](https://user-images.githubusercontent.com/132557392/236205607-a7e521ec-be16-41ab-aa2f-9f05422a50a6.png)

# Bar Chart for Programming Skills in Data Scientist Roles
![image](https://user-images.githubusercontent.com/132557392/236205657-a2c922ac-f15e-48f5-9666-a616a7d9d191.png)

# Bar Chart for Software Skills in Data Scientist Roles
![image](https://user-images.githubusercontent.com/132557392/236205691-20eddcc2-7e19-464b-a259-cac5f99c3d6c.png)

# Bar Chart for Programming Skills in Data Engineer Roles
![image](https://user-images.githubusercontent.com/132557392/236205740-e15ebade-629e-4578-9ca1-287016de01df.png)

# Bar Chart for Software Skills in Data Engineer Roles
![image](https://user-images.githubusercontent.com/132557392/236205775-e1a8cc40-9bd3-464b-b4f7-b88d6e116caf.png)
