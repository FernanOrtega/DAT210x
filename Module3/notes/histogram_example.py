#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:47:53 2017

@author: fernando
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv("/home/fernando/CoursePythonDS/DAT210x/Module3/Datasets/wheat.data")

print df.describe()

df[df.groove>5].asymmetry.plot.hist(alpha=0.3, normed=True)
df[df.groove<=5].asymmetry.plot.hist(alpha=0.5, normed=True)
plt.show()