# [DataSkills](https://abdealib520-dataskills-main-i93jq5.streamlit.app/)
This is a website that i created that will tell you what kind of skills are required in the Data Science industry based on data taken from real world jobs.

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
![image](https://user-images.githubusercontent.com/132557392/236204327-282c8603-5584-4bc6-92af-3c165f59fadd.png)

# Bar Chart for Programming Skills in Data Scientist Roles
![image](https://user-images.githubusercontent.com/132557392/236204490-4aee5e16-ffca-42d0-87c2-eaed5067f3c2.png)

# Bar Chart for Software Skills in Data Scientist Roles
![image](https://user-images.githubusercontent.com/132557392/236204633-3b83ffb5-a164-488e-9861-9b65b797c0dc.png)

# Bar Chart for Programming Skills in Data Engineer Roles
![image](https://user-images.githubusercontent.com/132557392/236204806-27f5e6e2-00d3-4b66-a029-43cfd5b40375.png)

# Bar Chart for Programming Skills in Data Engineer Roles
![image](https://user-images.githubusercontent.com/132557392/236204836-ee4b6805-f9f8-45e6-a92a-0702888cf603.png)
