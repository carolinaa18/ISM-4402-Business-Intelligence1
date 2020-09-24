#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,0,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
    columns=['Names', 'Grades'])

df.loc[df['Grades'] >= 0] 









# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




