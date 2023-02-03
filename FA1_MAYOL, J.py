#!/usr/bin/env python
# coding: utf-8

# In[36]:


import os

print("Calculator for Miles, Average Pace, and Average Speed\n")

km = float(input('Type the number of kilometers: '))
mi = km/1.61
roundmi = round(mi, 4)
min = float(input('How many minutes? '))
sec_in = float(input('How many additional seconds? '))
sec = min*60+sec_in

avg_pace = (sec/mi)/60
round_pace = round(avg_pace, 4)
hrs = sec/60/60
avg_speed = mi/hrs
round_speed = round(avg_speed, 4)

print("\n2.)\nThere are", roundmi, "miles in", km, "kilometers.")
print("\n3.)\nYour average pace is", round_pace, "minutes and seconds per mile.")
print("Your average speed is", round_speed, "miles per hour.\n")
os.system("pause")


# In[ ]:




