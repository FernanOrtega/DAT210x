import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
df = pd.read_csv('Datasets/espn.csv', sep='\t', skiprows=1)

# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
df.columns = ['RK', 'PLAYER', 'TEAM', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM', 
'PTS/G', 'SOG', 'PCT', 'GWG', 'PP/G', 'PP/A', 'SH/G', 'SH/A']


# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
df = df.dropna(axis=0, thresh=4)


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#

df = df.loc[df.RK != 'RK']


# TODO: Get rid of the 'RK' column
#
df = df.drop(labels=['RK'], axis=1)


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
df = df.reset_index(drop = True)



# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
print df.dtypes

df = df.apply(pd.to_numeric, errors='ignore')

print df.dtypes


# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# Number of rows
print df.shape[0]
print df.iloc[:,0].count()

# Unique PCT values
print len(df.PCT.unique())

# What is the value you get by adding the GP values at indices 15 and 16 of this table?
print df.loc[15:16, 'GP'].sum()