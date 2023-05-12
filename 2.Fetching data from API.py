#!/usr/bin/env python
# coding: utf-8

# # Importing Necessary Libraries

# In[1]:


import pandas as pd
import requests      #requests module allows us to send HTTP requests using Python


# # Requesting To web page

# In[2]:


response=requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=ca54aee55c18784983c9e78edfe3a45f&language=en-US&page=1')


# # Convert incoming Data To JSON format

# In[3]:


response.json()


# In[4]:


#want a particular key named result 
response.json()['results']


# In[5]:


#convert to dataframe
pd.DataFrame(response.json()['results'])


# In[6]:


#extract only those columns wanted
pd.DataFrame(response.json()['results'])[['id','popularity', 'title', 'vote_average','vote_count']]


# In[7]:


#store in a dataframe named temp_df
temp_df=pd.DataFrame(response.json()['results'])[['id','popularity', 'title', 'vote_average','vote_count']]


# In[8]:


#print temp_df
temp_df


# # Do the Entire process in a loop 

# In[9]:


#Make an empty data frame named df
df=pd.DataFrame()


# In[10]:


df


# In[11]:


for i in range(1,429):
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}'.format(i))
    temp_df=pd.DataFrame(response.json()['results'])[['id','popularity', 'title', 'vote_average','vote_count']]
    df = pd.concat([df,temp_df],ignore_index=True)


# In[12]:


df


# In[13]:


df.shape


# In[14]:


#convert this dataframe to CSV
df.to_csv('movies.csv')

