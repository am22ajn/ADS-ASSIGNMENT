
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv(r"/content/florida-history.csv")
data

data.columns

data.tail()

data.describe()

data.isnull().sum()

import pandas as pd
import matplotlib.pyplot as plt

# read the COVID-19 data from csv file
#covid_data = pd.read_csv('covid_data.csv')

# convert the date column to datetime objects
data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')

def plot_cases_by_state():
    # group the data by state and sum the cases
    state_cases = data.groupby('state')['totalTestResults'].sum().sort_values(ascending=False)[:10]

    # create a bar chart with the top 10 states by cases
    plt.bar(state_cases.index, state_cases.values)

    # customize the legend
    plt.title('Top 10 States by Total COVID-19 Cases')
    plt.xlabel('State')
    plt.ylabel('Total Cases')
    plt.legend(['Total Cases'])
    plt.show()


def plot_cases_by_date():
    # group the data by date and sum the cases
    date_cases = data.groupby('date')['totalTestResults'].sum()

    # create a line chart of cases over time
    plt.plot(date_cases.index, date_cases.values)

    # customize the legend
    plt.title('Total COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.legend(['Total Cases'])
    plt.show()


def plot_deaths_by_state():
    # group the data by state and sum the deaths
    state_deaths = data.groupby('state')['death'].sum().sort_values(ascending=False)[:10]

    # create a bar chart with the top 10 states by deaths
    plt.bar(state_deaths.index, state_deaths.values)

    # customize the legend
    plt.title('Top 10 States by Total COVID-19 Deaths')
    plt.xlabel('State')
    plt.ylabel('Total Deaths')
    plt.legend(['Total Deaths'])
    plt.show()


def plot_deaths_by_date():
    # group the data by date and sum the deaths
    date_deaths = data.groupby('date')['death'].sum()

    # create a line chart of deaths over time
    plt.plot(date_deaths.index, date_deaths.values)

    # customize the legend
    plt.title('Total COVID-19 Deaths Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Deaths')
    plt.legend(['Total Deaths'])
    plt.show()
def plot_cases_and_deaths_by_date():
    # group the data by date and sum the cases and deaths
    date_data = data.groupby('date')[['totalTestResults', 'death']].sum()

    # create a line chart of cases and deaths over time
    plt.plot(date_data.index, date_data['totalTestResults'], label='Total Cases')
    plt.plot(date_data.index, date_data['death'], label='Total Deaths')

    # customize the legend
    plt.title('Total COVID-19 Cases and Deaths Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases/Deaths')
    plt.legend()

    plt.show()

plot_cases_by_state()

plot_cases_by_date()

plot_deaths_by_date()

plot_deaths_by_state()

plot_cases_and_deaths_by_date()

"""# New Section

# New Section
"""