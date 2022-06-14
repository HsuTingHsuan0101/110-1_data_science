#!/usr/bin/env python
# coding: utf-8

# # Counting:

# In[1]:


fruit_list = ['apple', 'apple', 'banana', 'apple', 'banana', 'grape', 'banana', 'apple']


# ## Using dictionary
# - `list.count(key)`

# In[2]:


# Method 1
fruit_count = {}
for fruit in fruit_list:
    if fruit not in fruit_count:
        fruit_count[fruit] = fruit_list.count(fruit)


# In[3]:


fruit_count


# In[6]:


# Method 2
fruit_count = dict()
for fruit in set(fruit_list):
    fruit_count[fruit] = fruit_list.count(fruit)


# In[7]:


fruit_count


# ## Using `Counter()`

# In[9]:


from collections import Counter


# In[12]:


fruit_count = Counter(fruit_list)


# In[14]:


for k, v in fruit_count.items():
    print(k, "\t", v)


# ## Comprehensive dictionary

# In[33]:


fruit_count = {k:fruit_list.count(k) for k in set(fruit_list)}
fruit_count


# # 從wikipedia引入資料

# In[15]:


import wikipedia


# In[23]:


string_a = wikipedia.summary("Big_data", sentences = 20)
string_a


# ### text processing

# In[24]:


import string


# In[25]:


# 拿掉標點符號
translator = str.maketrans('', '', string.punctuation)
string_a = string_a.translate(translator)
string_a


# In[26]:


# 轉小寫
string_a = string_a.lower()
print(string_a)


# In[28]:


words = string_a.split()
words[:10]


# In[31]:


words_freq = Counter(words)
print(len(words_freq))
print(words_freq)

value_freq = Counter(words_freq.values())
print(value_freq)


# In[ ]:




