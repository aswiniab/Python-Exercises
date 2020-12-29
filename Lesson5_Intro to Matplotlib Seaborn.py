#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 12:15:20 2020

Description: Intro to Matplotlib and Seaborn

@author: aswiniabraham
"""
'''
Summary
plt.plot()- line chart
plt.bar()- bar chart
plt.hist()- histogram
Use matplotlib for line and histogram. Use seaborn for the rest
'''
import matplotlib.pyplot as plt
import seaborn as sns
# to ensure plots are shown in line with output instead of popups
%matplotlib inline 

# LINE CHART
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
year = [2010, 2011, 2012, 2013, 2014, 2015]
plt.plot(year, yield_apples)
plt.xlabel('Year')
plt.ylabel('Yield');
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
year= range(2000,2012)  # years from 2000 to 2011
# Markers: https://matplotlib.org/3.1.1/api/markers_api.html
# Styling: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
plt.plot(year, apples, marker='o', c='b', ls='--',lw=2,ms=8, mew=2, mec='navy')
plt.plot(year, oranges, marker='x', c='r', ls='--', lw=3, ms=10, alpha=.5)
plt.xlabel('Years')
plt.ylabel('Yield')
plt.title('Crop yields in ABC')
plt.legend(['Apples','Oranges']);
#shortcut for marker shape, line shape, line style, line color. enter as 3rd argument or fmt='s--b'
plt.plot(year, apples, 's--b' )
plt.plot(year, oranges, 'o-r')
plt.xlabel('Years')
plt.ylabel('Yield')
plt.title('Crop yields in ABC')
plt.legend(['Apples','Oranges']);
plt.plot(year, oranges, 'or')
plt.figure(figsize=(24,12));

# seaborn: https://seaborn.pydata.org/generated/seaborn.set_style.html
sns.set_style('whitegrid')
sns.set_style('darkgrid')
plt.plot(year, apples, 's--b' )
plt.plot(year, oranges, 'o-r')
plt.xlabel('Years')
plt.ylabel('Yield')
plt.title('Crop yields in ABC')
plt.legend(['Apples','Oranges']);

#edit defaul styles
import matplotlib
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

# SCATTER PLOT
flowers_df=sns.load_dataset('iris')
flowers_df
plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)
plt.title('Sepal dimensions')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
sns.scatterplot(x=flowers_df.sepal_length, 
                y=flowers_df.sepal_width, 
                hue=flowers_df.species, 
                s=100);
#or
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', s=100,data=flowers_df);

# HISTOGRAM
plt.hist(flowers_df.sepal_length)
plt.hist(flowers_df.sepal_width)
import numpy as np
plt.hist(flowers_df.sepal_width, bins=np.arange(2,5,0.25))

plt.hist(flowers_df[flowers_df.species == 'setosa'].sepal_width,alpha=0.4, bins=np.arange(2, 5, 0.25) )
plt.hist(flowers_df[flowers_df.species == 'versicolor'].sepal_width,alpha=0.4, bins=np.arange(2, 5, 0.25) )
plt.legend(['Setosa','Versicolor']);

# BAR CHART
years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]
plt.plot(years,apples, 'o--r')
plt.bar(years,apples);

plt.bar(years,apples)
plt.bar(years,oranges, bottom=apples);

tips_df = sns.load_dataset("tips");
tips_df
# average bill f each day
sns.barplot(x='day',y='total_bill',hue='sex', data=tips_df);


# HEAT MAP
flights_df = sns.load_dataset("flights")
flights_df=flights_df.pivot("month", "year", "passengers")
flights_df
sns.heatmap(flights_df, annot=True, cmap='Blues')
sns.heatmap(flights_df, fmt='d',annot=True, cmap='Blues')

# IMAGES
from urllib.request import urlretrieve
urlretrieve('https://i.imgur.com/SkPbq.jpg', 'chart.jpg');
from PIL import Image
img = Image.open('chart.jpg')
img
img_array = np.array(img)
img_array.shape
# display image in file
plt.imshow(img);
# turn off grid and axis
plt.grid(False)
plt.title('A data science meme')
plt.axis('off')
plt.imshow(img);
# zoom into the image
plt.grid(False)
plt.axis('off')
plt.imshow(img_array[125:325,105:305]);

# MULTIPLE PLOTS IN A GRID FORMAT
fig, axes = plt.subplots(2,3, figsize=(16,8))
# Use the axes for plotting
axes[0,0].plot(years, apples, 's-b')
axes[0,0].plot(years, oranges, 'o--r')
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('Yield (tons per hectare)')
axes[0,0].legend(['Apples', 'Oranges']);
axes[0,0].set_title('Crop Yields in Kanto')


# Pass the axes into seaborn
axes[0,1].set_title('Sepal Length vs. Sepal Width')
sns.scatterplot(x=flowers_df.sepal_length, 
                y=flowers_df.sepal_width, 
                hue=flowers_df.species, 
                s=100, 
                ax=axes[0,1]);

# Use the axes for plotting
axes[0,2].set_title('Distribution of Sepal Width')
axes[0,2].hist([flowers_df[flowers_df.species=='setosa'].sepal_width, 
                flowers_df[flowers_df.species=='versicolor'].sepal_width, 
                flowers_df[flowers_df.species=='virginica'].sepal_width], 
                bins = np.arange(2, 5, 0.25), stacked=True);

axes[0,2].legend(['Setosa', 'Versicolor', 'Virginica']);

# Pass the axes into seaborn
axes[1,0].set_title('Restaurant bills')
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df, ax=axes[1,0]);

# Pass the axes into seaborn
axes[1,1].set_title('Flight traffic')
sns.heatmap(flights_df, cmap='Blues', ax=axes[1,1]);

# Plot an image using the axes
axes[1,2].set_title('Data Science Meme')
axes[1,2].imshow(img)
axes[1,2].grid(False)
axes[1,2].set_xticks([])
axes[1,2].set_yticks([])

plt.tight_layout(pad=2);


# PAIR PLOTS
sns.pairplot(flowers_df, hue='species');
sns.pairplot(tips_df, hue='sex');
