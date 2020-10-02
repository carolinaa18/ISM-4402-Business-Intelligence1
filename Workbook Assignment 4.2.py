#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
Location = "gradedata.csv"
df = pd.read_csv(Location)
df.head()

import numpy as np
df['timemgmt'] = np.where((df['exercise']>3)
& (df['hours'] > 17),'busy', 'not busy')
df


# In[ ]:





# In[ ]:




