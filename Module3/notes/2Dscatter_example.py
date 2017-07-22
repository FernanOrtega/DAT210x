#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:14:57 2017

@author: fernando
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv('concrete.csv')

print df.describe()



# Plot 1
df.plot.scatter(x='cement', y='strength')
plt.suptitle('Cement vs str')
plt.xlabel('Cement')
plt.ylabel('Str')

# Plot 2
df.plot.scatter(x='slag', y='strength')
plt.suptitle('slag vs str')
plt.xlabel('slag')
plt.ylabel('Str')

# Plot 3
df.plot.scatter(x='ash', y='strength')
plt.suptitle('ash vs str')
plt.xlabel('ash')
plt.ylabel('Str')

# Plot 4
df.plot.scatter(x='water', y='strength')
plt.suptitle('water vs str')
plt.xlabel('water')
plt.ylabel('Str')

# Plot 5
df.plot.scatter(x='superplastic', y='strength')
plt.suptitle('superplastic vs str')
plt.xlabel('superplastic')
plt.ylabel('Str')

# Plot 6
df.plot.scatter(x='coarseagg', y='strength')
plt.suptitle('coarseagg vs str')
plt.xlabel('coarseagg')
plt.ylabel('Str')

# Plot 7
df.plot.scatter(x='fineagg', y='strength')
plt.suptitle('fineagg vs str')
plt.xlabel('fineagg')
plt.ylabel('Str')

# Plot 8
df.plot.scatter(x='age', y='strength')
plt.suptitle('age vs str')
plt.xlabel('age')
plt.ylabel('Str')

plt.show()