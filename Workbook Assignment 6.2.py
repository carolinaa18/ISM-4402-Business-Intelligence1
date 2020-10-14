#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
Location = "gradedata.csv"
df = pd.read_csv(Location)
df.head()

import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ age + exercise + hours',
data=df).fit()
result.summary()

import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ exercise + hours',
data=df).fit()
result.summary()

import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ age + exercise + gender + hours ',
data=df).fit()
result.summary()


# In[ ]:





# In[ ]:




