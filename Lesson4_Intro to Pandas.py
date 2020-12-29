#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:40:55 2020
Description: Introduction to Pnadas
@author: aswiniabraham
"""

import pandas as pd
from urllib.request import urlretrieve
urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/italy-covid-daywise.csv', 'italy-covid-daywise.csv')

covid_df = pd.read_csv('italy-covid-daywise.csv')

print(type(covid_df))
print(covid_df)
covid_df.info()
covid_df.describe()
covid_df.columns
covid_df.shape
# Column selection
covid_df['new_cases']
covid_df.new_cases
# row selction
covid_df.loc[244]
# Cell selection
covid_df.at[244,'new_cases']
covid_df['new_cases'][244]
covid_df["new_cases"][244] # same as above
# covid_df[244]['new_cases'] - error, gives output 244
covid_df_copy = covid_df.copy()
#select subset of columns
covid_subset_columns = covid_df[['date','new_cases']] # pass list of columns []
covid_subset_columns

covid_df.head(3)

covid_df.new_tests.first_valid_index()
covid_df.loc[108:115]

# Random sample
covid_df.sample(5)
covid_df.sample(5)


# Sum
total_cases = covid_df.new_cases.sum()
total_cases
total_deaths=covid_df.new_deaths.sum()
total_deaths
death_rate = total_deaths/total_cases
death_rate

total_tests=covid_df.new_tests.sum()+935310
positivity_rate=total_cases/total_tests
positivity_rate
print('{:.2f}% of tests conducted turned postive'.format(positivity_rate*100))

# Select new cases where number of cases are > 1000
select_temp = covid_df.new_cases > 1000
select_temp
covid_df[select_temp]
# Days in which the number cof casees > 1000
covid_df[select_temp].date

covid_df[covid_df.new_cases/covid_df.new_tests > positivity_rate]
# add new column to data frame
covid_df['positivity_rate']= covid_df.new_cases / covid_df.new_tests
covid_df

# drop a column
covid_df.drop(columns=['positivity_rate'], inplace=True)
covid_df
# Sorting
covid_df.sort_values('new_cases', ascending=False).head(5)
# Editing dataset
covid_df.sort_values('new_cases', ascending=True).head(5)

# Missing / faulty data
# 1. Replace with zero
# 2. Replace with average of column
# 3. Replace with average of just preceeding and succeeding values - works for time series data
# 4. Discard row completely

# Edit cell value
covid_df.at[172,'new_cases']= (covid_df.new_cases[171]+covid_df.new_cases[173])/2
covid_df.at[172,'new_cases']

# WORKING WITH DATES
#Tell python that 'date' is a variable of date datatype
covid_df['date'] = pd.to_datetime(covid_df.date)
covid_df['date']
# extracting year, month, day
covid_df['year']= pd.DatetimeIndex(covid_df.date).year
covid_df['month']=pd.DatetimeIndex(covid_df.date).month_name()
covid_df['day']=pd.DatetimeIndex(covid_df.date).day
covid_df['weekday']=pd.DatetimeIndex(covid_df.date).weekday
covid_df
# Find sum of new cases, daeaths and tests in month of May
covid_df_may = covid_df[covid_df.month == 'May']
covid_df_may
# sum of cases in May
covid_df_may_subset= covid_df_may[['new_cases','new_deaths','new_tests']]
covid_df_may_subset_totals = covid_df_may_subset.sum()
covid_df_may_subset_totals
covid_df[covid_df.month == 'May'][['new_cases', 'new_deaths', 'new_tests']].sum() # alternate concise code
covid_df.new_cases.mean()

# Grouping and aggregation
# find monthwise sum of data
covid_monthly= covid_df.groupby(covid_df.month)[['new_cases', 'new_deaths', 'new_tests']].sum()
covid_monthly
#cumulative cases
covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df

# Merging data from different sources
urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 'location.csv')
location_df = pd.read_csv('location.csv')
location_df
covid_df['location']='Italy'
covid_df
merged_df = covid_df.merge(location_df,on='location')
merged_df # displayed only few columns
# Display full output
from IPython.display import display
with pd.option_context('display.max_columns', 15):display(merged_df)
merged_df['cases_per_million']= merged_df.total_cases*1e6 / merged_df.population
merged_df
merged_df.drop(columns = ['cases per million'] , inplace=True) # delete the column created by mistake

# Writing data back to files
merged_df.columns # display column names
results_df = merged_df[['date', 'new_cases', 'new_deaths', 'new_tests','total_cases', 'location','population','cases_per_million']]
import os
os.chdir('/Users/aswiniabraham/Documents/GitHub/Python')
results_df.to_csv('lesson4_results.csv',index=False)

# Plots
covid_df.new_cases.plot()
covid_df.set_index('date', inplace=True)
with pd.option_context('display.max_columns', 15):display(covid_df)
covid_df.new_cases.plot()
covid_df.new_deaths.plot(); #selecting the two code lines and running with lot both graphs on same frame
covid_monthly.new_cases.plot() # line graph
covid_monthly.new_cases.plot(kind='bar') # bar graph


