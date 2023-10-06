# 不要馬上run這邊的程式碼，這支code先整個看過一遍再作業
import pandas as pd
from tqdm import tqdm_notebook
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
import time
import seaborn as sns
from sklearn.cluster import KMeans

c = open('PUBG_MatchData_Flattened.tsv')
player_death = pd.read_csv(c,sep = '\t')

erangel = player_death[player_death['map_id'] == 'ERANGEL'].reset_index(drop = True)

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_killer_user_profile_url',axis = 1)
        
    except:
        0

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_killer_user_profile_url',axis = 1)
    except:
        0

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_killer_participant_id',axis = 1)
    except:
        0

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_victim_participant_id',axis = 1)
    except:
        0

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_victim_user_profile_url',axis = 1)
    except:
        0

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_killer',axis = 1)
    except:
        0

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_victim_user_nickname',axis = 1)
    except:
        0

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_killer_user_nickname',axis = 1)
    except:
        0

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_is_range_valid',axis = 1)
    except:
        0

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_killer_rank',axis = 1)
    except:
        0

for i in tqdm_notebook(range(123)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_victim_rank',axis = 1)
    except:
        0

for i in tqdm_notebook(range(100,123,1)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_description',axis = 1)
    except:
        0

for i in tqdm_notebook(range(100,123,1)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_killer_position_x',axis = 1)
    except:
        0

for i in tqdm_notebook(range(100,123,1)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_killer_position_y',axis = 1)
    except:
        0

for i in tqdm_notebook(range(100,123,1)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_time_event',axis = 1)
    except:
        0

for i in tqdm_notebook(range(100,123,1)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_victim_position_x',axis = 1)
    except:
        0

for i in tqdm_notebook(range(100,123,1)):
    try:
        erangel = erangel.drop('deaths_'+str(i)+'_victim_position_y',axis = 1)
    except:
        0

deaths = pd.DataFrame({})
for i in tqdm_notebook(range(100)):
    each_data = erangel[['deaths_'+str(i)+'_description','deaths_'+str(i)+'_killer_position_x','deaths_'+str(i)+'_killer_position_y','deaths_'+str(i)+'_time_event','deaths_'+str(i)+'_victim_position_x','deaths_'+str(i)+'_victim_position_y']]
    each_data = each_data.rename(columns={'deaths_'+str(i)+'_description':'deaths_description','deaths_'+str(i)+'_killer_position_x':'deaths_killer_position_x','deaths_'+str(i)+'_killer_position_y':'deaths_killer_position_y','deaths_'+str(i)+'_time_event':'deaths_time_event','deaths_'+str(i)+'_victim_position_x':'deaths_victim_position_x','deaths_'+str(i)+'_victim_position_y':'deaths_victim_position_y'})
    deaths = pd.concat([deaths,each_data],ignore_index = True)

deaths.dropna(axis=0, how='any', inplace=True)
deaths = deaths[deaths['deaths_killer_position_x'] != 0].reset_index(drop = True)
deaths = deaths[deaths['deaths_victim_position_x'] != 0].reset_index(drop = True)
deaths = deaths.reset_index(drop = True)

# Category
a=deaths.groupby(['deaths_description'],as_index=False)['deaths_description'].agg({'val':'count'})
a=a.reset_index()
a=a.sort_values(by='val',ascending=False).reset_index(drop=True)
handgun = sum(a[a['deaths_description'].isin(['P18C','P1911','R1895','P92','R45'])]['val'])
AssaultRifle = sum(a[a['deaths_description'].isin(['AKM','AUG','Groza','M416','M16A4','SCAR-L'])]['val'])
Sniper = sum(a[a['deaths_description'].isin(['AWM','Kar98k','M24','SKS','MK14','Mini14', 'VSS'])]['val'])
SubMachineGun = sum(a[a['deaths_description'].isin(['TommyGun','MicroUZI','UMP9','Vector'])]['val'])
ShotGun = sum(a[a['deaths_description'].isin(['S1897','S686','S12K'])]['val'])
LightMachineGun = sum(a[a['deaths_description'].isin(['M249','DP28'])]['val'])
MeleeWeapon = sum(a[a['deaths_description'].isin(['Punch','Pan','Crowbar','Sickle','Machete'])]['val'])
Vehicle = sum(a[a['deaths_description'].isin(['Aquarail','Boat','Buggy','Dacia','Motorbike', 'Motorbike(SideCar)','Uaz'])]['val'])
ThrowableWeapon = sum(a[a['deaths_description'].isin(['Grenade','death.ProjMolotov_DamageField_C'])]['val'])
Accident = sum(a[a['deaths_description'].isin(['Bluezone','Drown','Falling','RedZone'])]['val'])
b = pd.DataFrame({'weapon':['handgun','AssaultRifle','Sniper','SubMachineGun','ShotGun','LightMachineGun' ,'MeleeWeapon','Vehicle','ThrowableWeapon','Accident'],
                 'kill':[handgun,AssaultRifle,Sniper,SubMachineGun,ShotGun,LightMachineGun,MeleeWeapon, Vehicle,ThrowableWeapon,Accident]})

# killer
killer = deaths[['deaths_killer_position_x','deaths_killer_position_y']]
position = killer.to_dict(orient='split')['data']
clf = KMeans(n_clusters=50)
a = time.time()
clf.fit(position)
b = time.time()
print(b-a)
killer = deaths[['deaths_killer_position_x','deaths_killer_position_y','deaths_description']]
killer['k-mean'] = clf.labels_
killer.to_csv('killer.csv',index=False)

# victim
# from sklearn import cluster, datasets
victim = deaths[['deaths_victim_position_x','deaths_victim_position_y']]
position = victim.to_dict(orient='split')['data']
clf = KMeans(n_clusters=50)
a = time.time()
# kmeans_fit = cluster.KMeans(n_clusters = 100).fit(victim)
clf.fit(position)
b = time.time()
print(b-a)
victim = deaths[['deaths_victim_position_x','deaths_victim_position_y','deaths_description']]
# victim['k-mean'] = kmeans_fit.labels_
victim['k-mean'] = clf.labels_
victim.to_csv('victim.csv',index=False)
