#!/usr/bin/env python
# coding: utf-8

# #### In this project, we'll work with a data set of submissions to popular technology site Hacker News.

# #### Hacker News is a site started by the startup incubator Y Combinator, where user-submitted stories (known as "posts") are voted and commented upon, similar to reddit. Hacker News is extremely popular in technology and startup circles, and posts that make it to the top of Hacker News' listings can get hundreds of thousands of visitors as a result.

# In[1]:


from csv import reader


# In[2]:


openfile = open("hacker_news.csv")
readfile = reader(openfile)
hn = list(readfile)
hn[1:5]


# #### Extract the first row of data

# In[3]:


headers = hn[0]
headers


# In[4]:


hn = hn[1:]
hn[0:5]


# Now that we've removed the headers from hn, we're ready to filter our data Now that we've removed the headers from hn, we're ready to filter our data

# In[5]:


ask_posts =  []
show_posts =  []
other_posts = []
for i in hn:
    title = i[1]
    title = title.lower()
    if title.startswith('ask hn') == True:
        ask_posts.append(i)
    elif title.startswith('show hn') == True:
        show_posts.append(i)
    else:
        other_posts.append(i)


# ### Check all posts

# In[6]:


ask_posts[0:5]


# In[7]:


show_posts[0:5]


# In[8]:


other_posts[0:5]


# ### Next, let's determine if ask posts or show posts receive more comments on average.

# #### comments on ask_posts

# In[9]:


total_ask_comments = 0
n_comments = 0
for i in ask_posts:
    comment =  int(i[4])
    total_ask_comments += comment
    n_comments += 1


# In[10]:


avg_ask_comments = total_ask_comments / n_comments
avg_ask_comments = float("{:.2f}".format(avg_ask_comments))
avg_ask_comments


# #### comments on show_posts

# In[11]:


total_show_comments = 0
m_comments = 0
for i in show_posts:
    comment = int(i[4])
    total_show_comments += comment
    m_comments += 1 


# In[12]:


avg_show_comments = total_show_comments / m_comments
avg_show_comments = float("{:.2f}".format(avg_show_comments))
avg_show_comments


# ### above you should've determined that, on average, ask posts receive more comments than show posts. Since ask posts are more likely to receive comments, we'll focus our remaining analysis just on these posts.

# ### calculating the amount of ask posts and comments by hour created. We'll use the datetime module to work with the data in the created_at column.

# In[13]:


import datetime as dt


# In[14]:


result_list = []
for i in ask_posts:
    created_at = i[6]
    comment = int(i[4])
    result_list.append([created_at,comment])


# In[15]:


result_list[0:5]


# In[16]:


counts_by_hour = {}
comments_by_hour = {}
for i in result_list:
    date_time = i[0]
    date_time = dt.datetime.strptime(date_time,"%m/%d/%Y %H:%M")
    hour = date_time.strftime('%H')
    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = i[1]
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += i[1]


# In[17]:


counts_by_hour


# In[18]:


comments_by_hour


# ### Let's use this format to create a list of lists containing the hours during which posts were created and the average number of comments those posts received.

# In[19]:


avg_by_hour = []
for i in comments_by_hour:
    avg_by_hour.append([i,comments_by_hour[i]/len(comments_by_hour)])


# In[20]:


avg_by_hour


# ###  this format makes it hard to identify the hours with the highest values. Let's finish by sorting the list of lists and printing the five highest values in a format that's easier to read.

# In[21]:


swap_avg_by_hour = []
for i in avg_by_hour:
    swap_avg_by_hour.append([i[1],i[0]])


# In[22]:


swap_avg_by_hour


# In[23]:


sorted_swap = sorted(swap_avg_by_hour,reverse = True)


# ### Top 5 Hours for Ask Posts Comments

# In[24]:


sorted_swap[0:5]


# In[25]:


for i in sorted_swap:
    i[1] = dt.datetime.strptime(i[1],"%H")
    i[1] = i[1].strftime("%H: %M.%S")
    i[0] = "{:.2f}".format(i[0])
    print(f''' avg_comments | time 
        {i[0]} | {i[1]}
    
    ''')


# ## Creating a post at "3:PM" on "Hacker News"  have a higher chance of receiving comments

# # So What I Cover In This Project :-
# 
# ### I set a goal for the project.
# ### I collected and sorted the data.
# ### I reformatted and cleaned the data to prepare it for analysis.
# ### I analyzed the data.

# In[ ]:




