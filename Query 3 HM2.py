#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd


# In[17]:


df = pd.read_csv('/Users/paolaantonicoli/Desktop/ADM/2020-Jan.csv', header = 'infer', nrows = 200000,parse_dates=['event_time'],
date_parser=pd.to_datetime)


# In[18]:


pd.options.display.min_rows = 999


# In[38]:


## Q3.1

def hap_brand():
    c = input()
    assert c in set(df['category_code'])
    df1 = df.loc[df['category_code']==c][['brand','product_id','price']]
    df1 = df1.drop_duplicates()
    return df1.groupby('brand').price.mean()





# In[39]:


hap_brand()


# In[11]:


df


# In[65]:


#Find, for each category, the brand with the highest average price. Return all the results in ascending order by price.

#Q3.2
df1 = df.groupby(['category_code','brand']).price.mean().reset_index(name="media")

df2= pd.DataFrame(columns=df1.columns)

for elem, frame in df1.groupby('category_code'):
    result = frame.sort_values('media',ascending=False).head(1)
    df2 = pd.concat([df2,result])

df2


# In[63]:


df1 = df.groupby(['category_code','brand']).price.mean().reset_index(name="media")

df1


# In[ ]:




