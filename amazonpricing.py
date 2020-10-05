#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup
import smtplib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


url = "https://www.amazon.in/dp/B07XD1ZFJ9/ref=Oct_DLandingS_rdp_15e74a5b"


# In[4]:


headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}


# In[5]:


page=requests.get(url,headers=headers)


# In[6]:


soup = BeautifulSoup(page.content,'html.parser')


# In[7]:


print(soup.title)


# In[8]:


print(soup.title.name)


# In[9]:


print(soup.find_all('p'))


# In[10]:


for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))


# In[11]:


for url in soup.find_all('a'):
    print(url.get('href'))


# In[12]:


price= soup.find(id="priceblock_ourprice")
price.get_text()
    


# In[13]:


cpprice = price.get_text()


# In[14]:


s=cpprice[2:10]


# In[15]:


s


# In[16]:


c = 24990.0


# In[17]:


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("jaintoshi29999@gmail.com","pagalpasta")
    subject="Price down"
    body="check the link price is now reduced: https://www.amazon.in/dp/B07XD1ZFJ9/ref=Oct_DLandingS_rdp_15e74a5b"
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail("jaintoshi29999@gmail.com","adamyajain29@gmail.com",msg)
    print("mail sent")
    server.quit()


# In[18]:


if (c==24990.0):
    send_mail()


# In[24]:


get_ipython().system('pip install schedule ')


# In[ ]:


import schedule
import time
schedule.every().day.at("12:30").do(send_mail)
while 1:
    schedule.run_pending() 
    time.sleep(1) 


# In[ ]:




