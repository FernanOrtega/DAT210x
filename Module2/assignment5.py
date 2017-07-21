import pandas as pd
import numpy as np


#
# TODO:
# Load up the dataset, setting correct header labels.
#

df = pd.read_csv('Datasets/census.data', names = ['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification'])

print df.head()
print df.dtypes

#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#

print df['education'].unique()
print df['age'].unique()
print df['capital-gain'].unique()
print df['race'].unique()
print df['capital-loss'].unique()
print df['hours-per-week'].unique()
print df['sex'].unique()
print df['classification'].unique()

df = df.replace('?', np.nan)
# df.replace(to_replace='?', value=np.nan, inplace=True)

df['capital-gain'] = pd.to_numeric(df['capital-gain'], errors = 'coerce')
# df['capital-gain'] = df['capital-gain'].astype('int')

print df.dtypes

#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). If you ever get confused, think to yourself
# what makes more sense generally---to represent such features with a
# continuous numeric type... or a series of categories?
#

print df['age'].describe()
print df['capital-gain'].describe()
print df['capital-loss'].describe()
print df['hours-per-week'].describe()

#nominal
df['education'] = df['education'].astype("category").cat.codes
df['race'] = df['race'].astype("category").cat.codes
df['sex'] = df['sex'].astype("category").cat.codes
df['classification'] = df['classification'].astype("category").cat.codes

#numerical to ordinal
age = [0,20,30,50,70,120]
labels = ['<=20', '<=30', '<=50', '<=70', '>70']
df.age = pd.cut(df.age, bins=age, labels=labels, include_lowest = True)

#
# TODO:
# Print out your dataframe
#
print df.shape[0]