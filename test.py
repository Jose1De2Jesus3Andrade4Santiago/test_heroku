#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
df = pd.read_csv("test.csv", encoding = 'latin-1')
print(df)
df.to_csv('out.csv', index=False)  


# In[ ]:





# In[ ]:




