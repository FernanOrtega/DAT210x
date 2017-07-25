import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import os
from sklearn import manifold

def Plot2D(T, title, x, y, num_to_plot=80):
  # This method picks a bunch of random samples (images in your case)
  # to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))

  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y], c=colors, marker='.',alpha=0.7)
  
def Plot3D(T, title, x, y, z, num_to_plot=80):
  # This method picks a bunch of random samples (images in your case)
  # to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111, projection = '3d')
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  ax.set_zlabel('Component: {0}'.format(z))
  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y],T[:,z], c=colors, marker='.',alpha=0.7)
  
def doIsomap(df, n_neighbors, n_components):
  iso = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components)
  iso.fit(df)
  result = iso.transform(df)
#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
  Plot2D(result, '2d scatter - manifold', 0, 1)
#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
  Plot3D(result, '3d scatter - manifold', 0, 1, 2)

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
samples = []
colors = []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
for fname in os.listdir('Datasets/ALOI/32'):
  path = os.path.join('Datasets/ALOI/32', fname)
  img = misc.imread(path)
  samples.append((img[::2,::2] / 255.0).reshape(-1))
  colors.append('b')


#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
for fname in os.listdir('Datasets/ALOI/32i'):
  path = os.path.join('Datasets/ALOI/32i', fname)
  img = misc.imread(path)
  samples.append((img[::2,::2] / 255.0).reshape(-1))
  colors.append('r')


#
# TODO: Convert the list to a dataframe
#
df = pd.DataFrame(samples)

#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#

doIsomap(df, 6, 3)
#doIsomap(df, 5, 3)
#doIsomap(df, 4, 3)
#doIsomap(df, 3, 3)
#doIsomap(df, 2, 3)
#doIsomap(df, 1, 3)

plt.show()