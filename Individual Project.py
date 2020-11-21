#!/usr/bin/env python
# coding: utf-8

# In[32]:


# import data from axisdata.csv
import pandas as pd
Location = "axisdata.csv"

df = pd.read_csv(Location)
df.head(500)
# avg cars sold per month
df['Cars Sold'].mean()
# max cars sold per month
df['Cars Sold'].max()
# min cars sold per month
df['Cars Sold'].min()
# avg cars sold per month by gender
df.loc[df['Gender']=='M']['Cars Sold'].mean(), df.loc[df['Gender']=='F']['Cars Sold'].mean()
# avg hours worked by people selling over 3 cars a month
df.loc[df['Cars Sold']>3]['Hours Worked'].mean()
# avgyears of experience 
df['Years Experience'].mean()
# avg cars sold a month by whether or not they have sales training
df.loc[df['SalesTraining']=='Y']['Cars Sold'].mean(), df.loc[df['SalesTraining']=='N']['Cars Sold'].mean()


# In[ ]:





# In[ ]:




