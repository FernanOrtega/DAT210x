import pandas as pd


#https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names


# 
# TODO: Load up the mushroom dataset into dataframe 'X'
# Verify you did it properly.
# Indices shouldn't be doubled.
# Header information is on the dataset's website at the UCI ML Repo
# Check NA Encoding
#
X = pd.read_csv('Datasets/agaricus-lepiota.data', names=['class','cap-shape',
'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 
'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-aring',
'stalk-surface-bring', 'stalk-color-aring', 'stalk-color-bring', 'veil-type',
'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 
'habitat'])

# INFO: An easy way to show which rows have nans in them
print X[pd.isnull(X).any(axis=1)]

# 
# TODO: Go ahead and drop any row with a nan
#
# .. your code here ..
print X.shape


#
# TODO: Copy the labels out of the dset into variable 'y' then Remove
# them from X. Encode the labels, using the .map() trick we showed
# you in Module 5 -- canadian:0, kama:1, and rosa:2
#
y = X['class']
X = X.drop('class', axis=1)


#
# TODO: Encode the entire dataset using dummies
#
X = pd.get_dummies(X)


# 
# TODO: Split your data into test / train sets
# Your test size can be 30% with random_state 7
# Use variable names: X_train, X_test, y_train, y_test
#
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7) 



#
# TODO: Create an DT classifier. No need to set any parameters
#
from sklearn import tree
dtc = tree.DecisionTreeClassifier()

 
#
# TODO: train the classifier on the training data / labels:
# TODO: score the classifier on the testing data / labels:
#

dtc.fit(X_train, y_train)

score = dtc.score(X_test, y_test)

print "High-Dimensionality Score: ", round((score*100), 3)


#
# TODO: Use the code on the course's SciKit-Learn page to output a .DOT file
# Then render the .DOT to .PNGs. Ensure you have graphviz installed.
# If not, `brew install graphviz`. If you can't, use: http://webgraphviz.com/.
# On Windows 10, graphviz installs via a msi installer that you can download from
# the graphviz website. Also, a graph editor, gvedit.exe can be used to view the
# tree directly from the exported tree.dot file without having to issue a call.
#
tree.export_graphviz(dtc.tree_, out_file='tree.dot', feature_names=X.columns)

from subprocess import call
call(['dot', '-T', 'png', 'tree.dot', '-o', 'tree.png'])


