#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:11:16 2017

@author: fernando
"""

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import pandas as pd
matplotlib.style.use('ggplot') # Look Pretty
# If the above line throws an error, use plt.style.use('ggplot') instead

df = pd.read_csv("concrete.csv")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('cement')
ax.set_ylabel('water')
ax.set_zlabel('Strength')

ax.scatter(df.cement, df.water, df['strength'], c='r', marker='.')
plt.show()