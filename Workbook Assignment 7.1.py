#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
df.plot()
displayText = "Wow"
xloc = 1
yloc = df['Grades'].max()
xtext = 8
ytext = -150
plt.annotate(displayText,
xy=(0, 70),
arrowprops=dict(facecolor='black',
shrink=0.05), 
xytext=(0, 70),             
xycoords=('axes fraction', 'data'),
textcoords='offset points')
df.plot()



# In[ ]:





# In[ ]:




