#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "gradedata.csv"
df = pd.read_csv(Location)
df.hist(column="age", by="gender")
df


# In[ ]:




