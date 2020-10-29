#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "gradedata.csv"
dataframe = pd.DataFrame({'grade':
np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['grade'])

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "gradedata.csv"
dataframe = pd.DataFrame({'hours':
np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['hours'])


# In[ ]:





# In[ ]:





# In[ ]:




