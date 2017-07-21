import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv('Datasets/wheat.data')

#
# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 

# Plot 1
df.plot.scatter(x='area', y='perimeter', marker='.')
plt.suptitle('Area vs perimeter')
plt.xlabel('Area')
plt.ylabel('Perimeter')

#
# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
# Plot 2
df.plot.scatter(x='groove', y='asymmetry', marker='^')
plt.suptitle('groove vs asymmetry')
plt.xlabel('groove')
plt.ylabel('asymmetry')


#
# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 
# Plot 3
df.plot.scatter(x='compactness', y='width', marker='o') 
plt.suptitle('compactness vs width')
plt.xlabel('compactness')
plt.ylabel('width')



# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.


plt.show()


