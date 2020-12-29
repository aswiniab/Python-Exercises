#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:00:37 2020

Description: Exploration of the german credit dataset

@author: aswiniabraham
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
sns.set_style('whitegrid')


german_df = pd.read_csv('/Users/aswiniabraham/Documents/2.MVA/Project/DataOriginal/german.data', delimiter=' ')
german_df
german_df.describe()
german_df.info()
from IPython.display import display
with pd.option_context('display.max_columns', 25):display(german_df.describe())

german_df.columns=['account_bal',	'duration',	'payment_status',	'purpose',	
                   'credit_amount',	'savings_bond_value',	'employed_since',
                   'intallment_rate',	'sex_marital',	'guarantor',	'residence_since',
                   'most_valuable_asset',	'age',	'concurrent_credits',	'type_of_housing',	
                   'number_of_existcr',	'job',	'number_of_dependents',	'telephon',	
                   'foreign',	'good_bad']
german_df.info()


# VISUALIZATION
good_bad_per=round(((german_df.good_bad.value_counts()/german_df.good_bad.count())*100))
good_bad_per
plt.pie(good_bad_per,labels=['Good loans', 'Bad loans'], autopct='%1.0f%%', startangle=90)
plt.title('Percentage of good and bad loans');

# CONTINUOUS PREDICTORS
fig, axes = plt.subplots(1,3, figsize=(16,8))
plt.suptitle('Histogram of continuous variables')
axes[0].hist(german_df['duration'])
axes[0].set_xlabel('No. of observations')
axes[0].set_ylabel('Years')
axes[0].set_title('Histogram of loan duration');

axes[1].hist(german_df['credit_amount'])
axes[1].set_xlabel('No. of observations')
axes[1].set_ylabel('Credit amount (dollars)')
axes[1].set_title('Histogram of Credit amount');

axes[2].hist(german_df['age'])
axes[2].set_xlabel('No. of observations')
axes[2].set_ylabel('Age')
axes[2].set_title('Histogram of Age');

#log of continues variables to normalise them
german_df.duration_t= np.log(german_df.duration)
german_df.credit_amount_t= np.log(german_df.credit_amount)
german_df.age_t= np.log(german_df.age)

fig, axes = plt.subplots(1,3, figsize=(16,8))
plt.suptitle('Histogram of transformed continuous variables')
axes[0].hist(german_df.duration_t)
axes[0].set_xlabel('No. of observations')
axes[0].set_ylabel('Years')
axes[0].set_title('Histogram of loan duration');

axes[1].hist(german_df.credit_amount_t)
axes[1].set_xlabel('No. of observations')
axes[1].set_ylabel('Credit amount (dollars)')
axes[1].set_title('Histogram of Credit amount');

axes[2].hist(german_df.age_t)
axes[2].set_xlabel('No. of observations')
axes[2].set_ylabel('Age')
axes[2].set_title('Histogram of Age');

# distribution plots using seaborn
fig, ax = plt.subplots(1,3,figsize=(20,5))
plt.suptitle('DISTRIBUTION PLOTS')
sns.distplot(german_df.duration_t, bins=40, ax=ax[0])
sns.distplot(german_df.credit_amount_t, bins=40, ax=ax[1], color='salmon')
sns.distplot(german_df.age_t, bins=40, ax=ax[2], color='darkviolet');

sns.barplot(x='payment_status', y='credit_amount', hue='good_bad',data=german_df);

#sns.countplot(german_df['payment_status'], hue=german_df['good_bad'],  palette='Greens');
sns.countplot(german_df['payment_status'], hue=german_df['good_bad']);
#sns.countplot(y=german_df['payment_status'], hue=german_df['good_bad'], orient='v');

# line chart

sns.lineplot(data=german_df, x='duration', y='credit_amount');
a= german_df.good_bad.unique()
