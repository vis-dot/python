# -*- coding: utf-8 -*-
"""vishalkrishikesh.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mZCa6Keq_3qaPQTyDBU4neJvwAYV144E
"""

a="""I am signing up for Replit's 100 days of Python challenge! I will make sure to spend 
some time every day coding along, for a minimum of 10 minutes a day. I'll be using 
Replit, an amazing online IDE so I can do this from my phone wherever I happend to be. 
No excuses for not coding from the middle of a field!"""
print(a)



m_d={
    "phising":"Emails can be disguised to be coming from a fraudulent company for the sole purpose of getting you to reveal personal information",
     "Malicious websites":"Some websites may attempt to install malware onto your computer, usually through popups or malicious links",
    "torrents":"File shared through the bittorrents to the of any system"
}
print(type(m_d))
print()


print(m_d)

mob_cost=12300
gst_per=18
gst_amount=(mob_cost/100)*gst_per
net_prise=mob_cost+gst_amount
print("gst cost",gst_amount)
print("net prise: ",net_prise)

import pandas as pd
data_set={
    "Offence":['Sending threatening message by email','Sending defamatory messages by email','Forgery of electronic records','Bogus websites, cyber frauds','Email spoofing','Web-Jacking','E-Mail Abuse','Online sale of Drugs','Online sale of Arms'],
    "Law":['Sec.503 IPC (Indian Penal Code)','Sec 499 IPC','Sec.463 IPC','Sec.420 IPC','Sec.463 IPC','Sec.383 IPC','Sec.500 IPC','Narcotic Drugs and Psychotropic Substances (NDPS) Act, 1985','Arms Act, 1959'],
    "Penalty":[2300,4000,"5 years jail","20 years jail",30000,2000000,54823,243004,4999],
    "media":['email','email','facebook','websites','email','google','instagram','tor web','tor web']
}
df=pd.DataFrame(data_set)
print(df)

def household():
  unit=int(input("\nNumber of Units used: "))

  if unit<100:
    price=unit*0.50
    print("Your Price : Rs.",price)
  elif unit>101 and unit<200:
    price=unit*0.75
    print("Your Price : Rs.",price)
  elif unit>201 and unit<300:
    price=unit*1.20
    print("Your Price : Rs.",price)
  else:
    price=unit*1.50
    print("Your Price : Rs.",price)

household()

import pandas as pd
df=pd.DataFrame({
"students name":['ram','rte','ws','sd','s','ad','as','af','we','jsdg'],
"DOB":[2000,2000,2000,2000,2001,2000,2001,2000,2001,2000],
"weight":[45,57,50,46,56,70,59,65,80,48],
"height":[1.76,1.80,3.98,2.10,2.23,2.00,3.68,2.59,5.78,7.70],
"age":[22,21,22,21,22,22,21,21,22,21],})
df["BMI"]=round(df['weight']/df['height'])
print(df)
