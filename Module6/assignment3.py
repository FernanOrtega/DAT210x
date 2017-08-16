import pandas as pd
from numpy import arange

## Question 1

# Step 1: Load data
X = pd.read_csv('Datasets/parkinsons.data')

# Step 2: splice state column and drop it out. Drop also the 'name' column
y = X['status']
X = X.drop(labels=['name', 'status'], axis=1)

# Step 3: Train&test splits
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7) 

# Step 4: Perform a SVC classifier
from sklearn.svm import SVC
model = SVC()
model.fit(X_train, y_train)

# Step 5: Scoring
score = model.score(X_test, y_test)

print 'Score with default parameters: ',score

## Question 2
best_score = 0
#best_C = 0.05
#best_gamma = 0.001
#best_scaler = 'None'
#best_pca_param = 0

# variable C from 0.05 to 2, using 0.05 unit increments. variable gamma from 0.001 to 0.1, using 0.001 unit increments.

## Question 3: use preprocessors
from sklearn import preprocessing
#listScaler = []
#listScaler.append(preprocessing.Normalizer())
#listScaler.append(preprocessing.MaxAbsScaler())
#listScaler.append(preprocessing.MinMaxScaler())
#listScaler.append(preprocessing.KernelCenterer())
#listScaler.append(preprocessing.StandardScaler())

#from sklearn.decomposition import PCA

#for scaler in listScaler:
#  scaler.fit(X_train)
#  t1X_train = scaler.transform(X_train)
#  t1X_test = scaler.transform(X_test)
#  for n_components in range(4, 15):
#    pca = PCA(n_components=n_components)
#    pca.fit(t1X_train)
#    tX_train = pca.transform(t1X_train)
#    tX_test = pca.transform(t1X_test)
#    for c in arange(0.05, 2.0, 0.05):
#      for g in arange(0.001, 0.1, 0.001):    
#        model = SVC(C=c, gamma=g)
#        model.fit(tX_train, y_train)
#        tscore = model.score(tX_test, y_test)
#        if tscore > best_score:
#          best_score = tscore
#          best_C = c
#          best_gamma = g
#          best_scaler = type(scaler)
#          best_pca_param = n_components
#      

#print 'C=',best_C,', gamma=',best_gamma, ', scaler=',best_scaler, 'pca_n_components=',best_pca_param


from sklearn import manifold

scaler = preprocessing.StandardScaler()
scaler.fit(X_train)
t1X_train = scaler.transform(X_train)
t1X_test = scaler.transform(X_test)

best_n = 0
best_c = 0

for n in range(2,6):
  for c in range(4,7):
    isomap = manifold.Isomap(n_neighbors=n, n_components=c)
    isomap.fit(t1X_train)
    tX_train = isomap.transform(t1X_train)
    tX_test = isomap.transform(t1X_test)
    model = SVC(C=1.65, gamma=0.098)
    model.fit(tX_train, y_train)
    tscore = model.score(tX_test, y_test)
    if tscore > best_score:
      best_score = tscore
      best_n = n
      best_c = c
      

print 'n_neighbors=',best_n,', n_components=',best_c
print 'Best score: ', best_score