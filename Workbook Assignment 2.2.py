#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'salesdata.db'
engine = create_engine(r"sqlite:///{}"
.format(db_file))
sql = 'select * from scores'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[ ]:




