#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#1. What is the northernmost airport in the United States?
airportsOriginal = pd.read_csv('airports.csv')
airports = airportsOriginal.copy()

northernmost = airports.sort_values(by = 'lat', ascending = False)
northernmost[(northernmost['lat'] > 0) &
             (northernmost['lon'] < 0) &
             (northernmost['tz'] <= -5) &
             (northernmost['tz'] >= -10)].head(1)


# In[3]:


#2. What is the easternmost airport in the United States?
easternmost = airports.sort_values(by = 'lon', ascending = False)
easternmost[(easternmost['lat'] > 0) &
            (easternmost['lon'] < 0) &
            (easternmost['tz'] <= -5) &
            (easternmost['tz'] >= -10)].head(1)


# In[4]:


#3. On February 12th, 2013, which New York area airport had the windiest weather?
weatherOriginal = pd.read_csv('weather.csv')
wind = weatherOriginal.copy()
wind = wind.sort_values(by = 'wind_speed', ascending = False)
wind[(wind['month'] == 2) &
     (wind['day'] == 12) &
     (wind['year'] == 2013) &
     (wind['wind_speed'] < 231)].head(1)


# In[ ]:


#In Summary:
#1. What is the northernmost airport in the United States?
#        Wiley Post-Will Rogers Memorial Airport
#2. What is the easternmost airport in the United States?
#        Eastport Municipal Airport
#3. On February 12th, 2013, which New York area airport had the windiest weather?
#        Laguardia Airport

