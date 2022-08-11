
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# import TDM for s1 and s2
import pickle
s1 = pd.read_pickle('../dat/tdm_stop_s1.pkl')
s2 = pd.read_pickle('../dat/tdm_stop.pkl')

tdm1 = s1.T
tdm2 = s2.T
tdm1['total_count'] = tdm1.sum(axis=1)
tdm1 = tdm1.sort_values(by='total_count', ascending=False)[0:25]
tdm2['total_count'] = tdm2.sum(axis=1)
tdm2 = tdm2.sort_values(by='total_count', ascending=False)[0:25]

# grouped bar plot for total number of words in s1 and s2
fig, ax = plt.subplots(figsize=(10,8))
plt.barh(tdm1.index, tdm1['total_count'], color='#5C64A2', alpha=0.5)
plt.barh(tdm2.index, tdm2['total_count'], color='#9A5E5D', alpha=0.5)
# invert y-axis
plt.gca().invert_yaxis()
plt.legend(['S1', 'S2'])
plt.title('Top 25 words in S1 and S2')
plt.ylabel('Count')
plt.show()

# top 25 words
# n=len(tdm1.index)
# r = np.arange(n)
# width = 0.05

# fig, ax = plt.subplots(figsize=(10,6))
# plt.bar(r, tdm1['total_count'], color='#5C64A2', alpha=0.5)
# plt.bar(r + width, tdm2['total_count'], color='#9A5E5D', alpha=0.5)
# plt.set_title('Top 25 words in S1 and S2')
# plt.set_ylabel('Number of words')
# plt.show()
