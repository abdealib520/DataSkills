import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class DataAnalyst():
    def __init__(self):
        self.df = pd.read_csv('Data Analyst.csv')
        self.data_languages = ['Python', 'R', 'SQL', 'Java', 'Scala', 'C++', 'JavaScript']
        self.softwares = ['Excel', 'Power BI', 'Tableau', 'SPSS', 'SAS', 'QlikView']

    def programming(self):
        D = dict()
        for i in self.data_languages:
            D[i] = self.df[i].sum() / len(self.df[i]) * 100
        keys = list(D.keys())
        values = list(D.values())
        sorted_value_index = np.argsort(values)[::-1]
        D = {keys[i]: values[i] for i in sorted_value_index}
        barchart = plt.figure(figsize=(12, 7))
        plt.bar(range(len(D)), list(D.values()), align='center',
                color=['#093c5f', '#064e80', '#0b6db0', '#078be6', '#078be6', '#078be6', '#078be6'])
        plt.xticks(range(len(D)), list(D.keys()))
        plt.ylabel('Percentage')
        return barchart

    def software(self):
        D = dict()
        for i in self.softwares:
            D[i] = self.df[i].sum() / len(self.df[i]) * 100
        keys = list(D.keys())
        values = list(D.values())
        sorted_value_index = np.argsort(values)[::-1]
        D = {keys[i]: values[i] for i in sorted_value_index}
        barchart = plt.figure(figsize=(12, 7))
        plt.bar(range(len(D)), list(D.values()), align='center',
                color=['#093c5f', '#064e80', '#0b6db0', '#078be6', '#078be6', '#078be6'])
        plt.xticks(range(len(D)), list(D.keys()))
        plt.ylabel('Percentage')
        return barchart

    def count(self):
        return len(self.df['job_title'])

    def cities(self):
        a = self.df['job_city'].value_counts()
        b = []
        rest = 0
        for i in a:
            if i < 10:
                rest += i
            else:
                b.append(i)
        b.append(rest)
        c = list(a.index)
        c = c[:6]
        c.append('Others')
        piechart = plt.figure(figsize=(10, 7))
        plt.pie(b, autopct='%1.1f%%', labels=c)
        return piechart


class DataScientist():
    def __init__(self):
        self.df = pd.read_csv('Data Scientist.csv')
        self.data_languages = ['Python', 'R', 'SQL', 'Java', 'Scala', 'C++', 'JavaScript']
        self.softwares = ['Excel', 'Power BI', 'Tableau', 'SPSS', 'SAS', 'QlikView']

    def programming(self):
        D = dict()
        for i in self.data_languages:
            D[i] = self.df[i].sum() / len(self.df[i]) * 100
        keys = list(D.keys())
        values = list(D.values())
        sorted_value_index = np.argsort(values)[::-1]
        D = {keys[i]: values[i] for i in sorted_value_index}
        barchart = plt.figure(figsize=(12, 7))
        plt.bar(range(len(D)), list(D.values()), align='center',
                color=['#093c5f', '#064e80', '#0b6db0', '#078be6', '#078be6', '#078be6', '#078be6'])
        plt.xticks(range(len(D)), list(D.keys()))
        plt.xlabel('Programming Languages')
        plt.ylabel('Percentage')
        return barchart

    def software(self):
        D = dict()
        for i in self.softwares:
            D[i] = self.df[i].sum() / len(self.df[i]) * 100
        keys = list(D.keys())
        values = list(D.values())
        sorted_value_index = np.argsort(values)[::-1]
        D = {keys[i]: values[i] for i in sorted_value_index}
        barchart = plt.figure(figsize=(12, 7))
        plt.bar(range(len(D)), list(D.values()), align='center',
                color=['#093c5f', '#064e80', '#0b6db0', '#078be6', '#078be6', '#078be6'])
        plt.xticks(range(len(D)), list(D.keys()))
        plt.xlabel('Softwares')
        plt.ylabel('Percentage')
        return barchart

    def count(self):
        return len(self.df['job_title'])

    def cities(self):
        a = self.df['job_city'].value_counts()
        b = []
        rest = 0
        for i in a:
            if i < 10:
                rest += i
            else:
                b.append(i)
        b.append(rest)
        c = list(a.index)
        c = c[:6]
        c.append('Others')
        piechart = plt.figure(figsize=(10, 7))
        plt.pie(b, autopct='%1.1f%%', labels=c)
        return piechart


class DataEngineer():
    def __init__(self):
        self.df = pd.read_csv('Data Engineer.csv')
        self.data_languages = ['Python', 'R', 'SQL', 'Java', 'Scala', 'C++', 'JavaScript']
        self.softwares = ['Excel', 'Power BI', 'Tableau', 'SAS', 'Apache Spark', 'Redshift', 'BigQuery', 'Airflow',
                          'Snowflake']

    def programming(self):
        D = dict()
        for i in self.data_languages:
            D[i] = self.df[i].sum() / len(self.df[i]) * 100
        keys = list(D.keys())
        values = list(D.values())
        sorted_value_index = np.argsort(values)[::-1]
        D = {keys[i]: values[i] for i in sorted_value_index}
        barchart = plt.figure(figsize=(12, 7))
        plt.bar(range(len(D)), list(D.values()), align='center',
                color=['#093c5f', '#064e80', '#0b6db0', '#078be6', '#078be6', '#078be6', '#078be6'])
        plt.xticks(range(len(D)), list(D.keys()))
        plt.xlabel('Programming Languages')
        plt.ylabel('Percentage')
        return barchart

    def software(self):
        D = dict()
        for i in self.softwares:
            D[i] = self.df[i].sum() / len(self.df[i]) * 100
        keys = list(D.keys())
        values = list(D.values())
        sorted_value_index = np.argsort(values)[::-1]
        D = {keys[i]: values[i] for i in sorted_value_index}
        barchart = plt.figure(figsize=(12, 7))
        plt.bar(range(len(D)), list(D.values()), align='center',
                color=['#093c5f', '#064e80', '#0b6db0', '#078be6', '#078be6', '#078be6', '#078be6', '#078be6',
                       '#078be6'])
        plt.xticks(range(len(D)), list(D.keys()))
        plt.xlabel('Software')
        plt.ylabel('Percentage')
        return barchart

    def count(self):
        return len(self.df['job_title'])

    def cities(self):
        a = self.df['job_city'].value_counts()
        b = []
        rest = 0
        for i in a:
            if i < 10:
                rest += i
            else:
                b.append(i)
        b.append(rest)
        c = list(a.index)
        c = c[:6]
        c.append('Others')
        piechart = plt.figure(figsize=(10, 7))
        plt.pie(b, autopct='%1.1f%%', labels=c)
        return piechart
