# victim.csv匯入這裡作業
import pandas as pd
from tqdm import tqdm_notebook
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
import time
import seaborn as sns

c = open('victim.csv')
victim = pd.read_csv(c)
victim = victim.loc[victim['deaths_description']!='DownandOut']
deaths = pd.DataFrame({})
for i in tqdm_notebook(range(1)):
    each_data = victim[['deaths_victim_position_x','deaths_victim_position_y','deaths_description','k-mean']]
    deaths = pd.concat([deaths,each_data],ignore_index = True)

res = pd.DataFrame({'分群':[],
                  '分群個數':[],
                  'Handgun':[],
                  'AssaultRifle':[],
                  'Sniper':[],
                  'SubMachineGun':[],
                  'ShotGun':[],
                  'LightMachineGun':[],
                  'MeleeWeapon':[],
                  'Vehicle':[],
                  'ThrowableWeapon':[],
                  'Accident':[]})


for i in range(50):
    
    death = deaths.loc[deaths['k-mean']==i]
    a=death.groupby(['deaths_description'],as_index=False)['deaths_description'].agg({'val':'count'})
    a=a.reset_index()
    a=a.sort_values(by='val',ascending=False).reset_index(drop=True)
    
    handgun = sum(a[a['deaths_description'].isin(['P18C','P1911','R1895','P92','R45'])]['val'])
    AssaultRifle = sum(a[a['deaths_description'].isin(['AKM','AUG','Groza','M416','M16A4','SCAR-L'])]['val'])
    Sniper = sum(a[a['deaths_description'].isin(['AWM','Kar98k','M24','SKS','MK14','Mini14',
                                                 'VSS'])]['val'])
    SubMachineGun = sum(a[a['deaths_description'].isin(['TommyGun','MicroUZI','UMP9','Vector'])]['val'])
    ShotGun = sum(a[a['deaths_description'].isin(['S1897','S686','S12K'])]['val'])
    LightMachineGun = sum(a[a['deaths_description'].isin(['M249','DP28'])]['val'])
    MeleeWeapon = sum(a[a['deaths_description'].isin(['Punch','Pan','Crowbar','Sickle','Machete'])]['val'])
    Vehicle = sum(a[a['deaths_description'].isin(['Aquarail','Boat','Buggy','Dacia','Motorbike',
                                                  'Motorbike(SideCar)','Uaz'])]['val'])
    ThrowableWeapon = sum(a[a['deaths_description'].isin(['Grenade','death.ProjMolotov_DamageField_C'])]['val'])
    Accident = sum(a[a['deaths_description'].isin(['Bluezone','Drown','Falling','RedZone'])]['val'])
    
    
    
    b = pd.DataFrame({'分群':[i],
                  '分群個數':[len(death)],
                    'x':[sum(death['deaths_victim_position_x'])/len(death)],
                    'y':[sum(death['deaths_victim_position_y'])/len(death)],
                  'Handgun':[round(handgun/len(death)*100,2)],
                  'AssaultRifle':[round(AssaultRifle/len(death)*100,2)],
                  'Sniper':[round(Sniper/len(death)*100,2)],
                  'SubMachineGun':[round(SubMachineGun/len(death)*100,2)],
                  'ShotGun':[round(ShotGun/len(death)*100,2)],
                  'LightMachineGun':[round(LightMachineGun/len(death)*100,2)],
                  'MeleeWeapon':[round(MeleeWeapon/len(death)*100,2)],
                  'Vehicle':[round(Vehicle/len(death)*100,2)],
                  'ThrowableWeapon':[round(ThrowableWeapon/len(death)*100,2)],
                  'Accident':[round(Accident/len(death)*100,2)]})
    
    
    res = pd.concat([res,b],ignore_index=True)
res.to_csv('victim_group.csv',encoding='utf_8_sig',index=False)
