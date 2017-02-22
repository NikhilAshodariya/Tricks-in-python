
# coding: utf-8

# In[60]:

import numpy as np
import pandas as pd
import csv
import warnings
warnings.simplefilter('ignore')


# In[61]:

def removeParticularElement(dataframe,col,element=0):
    df=dataframe
    e=element
    
    
    #df.sample(1)
    #df=df.ix[df['Calories'] >100]
    #df = df.drop(df[df.Calories < '100'].index)
    #df.Calories.astype(float)
    #df=df.ix[df['Calories'] >100]
    #col=df.columns[2:13]
    #print(col)
    #len(col)
    
    
    #here i have assumed to be ten columns to reduce my work you can modifiy it little bit for unknown number of columns
    modifiedFrame=df.ix[~((df[col[0]].astype(float)==e) & (df[col[1]].astype(float)==e) &
             (df[col[2]].astype(float)==e) & (df[col[3]].astype(float)==e) &
             (df[col[4]].astype(float)==e) & (df[col[5]].astype(float)==e) &
             (df[col[6]].astype(float)==e) & (df[col[7]].astype(float)==e) &
             (df[col[8]].astype(float)==e) & (df[col[9]].astype(float)==e) &
             (df[col[10]].astype(float)==e))]

    df=df[df.index.isin(modifiedFrame.index)]
    return df


# In[62]:

def removeMissingEntries(dataframe,colname,indicationOfMissing='----'):
    df=dataframe
    #df.Calories.astype(float)
    #dt[dt$Colname != indicationOfMissing, ]
    
    #colname is string
    #temp=subset(df, colname!=indicationOfMissing)
    #print(df.sample())
    #temp=df[colname].str.con.
    
    temp=df.ix[~(df[colname].str.contains(indicationOfMissing))]
    temp=df[df.index.isin(temp.index)]
    #print(mel_count)
    return temp
    


# In[63]:

def checkForDiabetes(dataframe,colname,checkRange,modifyCol=None,inRangeValue='yes',outOfRangeValue='no'):
    df=dataframe
    
    inRange=df.ix[((df[colname]>checkRange[0]) & (df[colname]<checkRange[1]))]
    outOfRange=df.ix[set(df.index)-set(inRange.index)]
    
    if modifyCol!=None:      
        outOfRange[modifyCol]=outOfRangeValue#Disease in our case as modifyCol
        inRange[modifyCol]=inRangeValue
    
    newFrame=pd.concat([inRange,outOfRange])
    return newFrame


# In[64]:

#milk, dairy, ghee, butter, buttermilk, cheese, paneer

def checkForItems(dataframe,colname,checkFor,modifyCol=None,inRangeValue='no',outOfRangeValue='yes'):
    df= dataframe
    
    #colname is food-item
    #here i have assumed to be six values columns to reduce my work you can modifiy it little bit for unknown number of columns
   
    inRange=df.ix[ df[colname].str.contains(checkFor[0]) | 
                   df[colname].str.contains(checkFor[1]) |
                   df[colname].str.contains(checkFor[2]) |
                   df[colname].str.contains(checkFor[3]) |
                   df[colname].str.contains(checkFor[4]) |
                   df[colname].str.contains(checkFor[5]) |
                   df[colname].str.contains(checkFor[6]) |
                   df[colname].str.contains(checkFor[7]) |
                   df[colname].str.contains(checkFor[8])
                 ]
    
    
    outOfRange=df.ix[set(df.index)-set(inRange.index)]
    
    if modifyCol!=None:      
        outOfRange[modifyCol]=outOfRangeValue#Disease in our case as modifyCol
        inRange[modifyCol]=inRangeValue
    
    newFrame=pd.concat([inRange,outOfRange])
    return newFrame
    


# In[65]:

def giveEatingTime(dataFrame,eb,b,l,s,d):
    df=dataFrame
    
    dfeb=df.ix[(df['food-item'].str.contains(eb[0]) & (df['Calories']<200))]
    dfeb['eb']=1
    
    dfb=df.ix[( (  df['food-item'].str.contains(b[0])|
                   df['food-item'].str.contains(b[1])|
                   df['food-item'].str.contains(b[2])|
                   df['food-item'].str.contains(b[3])|
                   df['food-item'].str.contains(b[4])|
                   df['food-item'].str.contains(b[5])|
                   df['food-item'].str.contains(b[6])|
                   df['food-item'].str.contains(b[7])|
                   df['food-item'].str.contains(b[8])
                 
                 ) & 
                 ( (df['Calories']>200) & (df['Calories']<950)))]
    dfb['b']=1
    
    
    dfl=df.ix[( (  df['food-item'].str.contains(b[0])|
                   df['food-item'].str.contains(b[1])|
                   df['food-item'].str.contains(b[2])|
                   df['food-item'].str.contains(b[3])|
                   df['food-item'].str.contains(b[4])
                 ) & 
                 ( (df['Calories']>700) & (df['Calories']<2500)))]
    dfl['l']=1
    
    
    dfs=df.ix[( (  df['food-item'].str.contains(b[0])|
                   df['food-item'].str.contains(b[1])|
                   df['food-item'].str.contains(b[2])|
                   df['food-item'].str.contains(b[3])|
                   df['food-item'].str.contains(b[4])|
                   df['food-item'].str.contains(b[5])
                 ) & 
                 ( (df['Calories']>500) & (df['Calories']<800)))]
    dfs['s']=1
    
    
    dfd=df.ix[( (  df['food-item'].str.contains(b[0])|
                   df['food-item'].str.contains(b[1])|
                   df['food-item'].str.contains(b[2])|
                   df['food-item'].str.contains(b[3])|
                   df['food-item'].str.contains(b[4])|
                   df['food-item'].str.contains(b[5])
                 ) & 
                 ( (df['Calories']>=650) & (df['Calories']<1800)))]
    dfd['d']=1
    
    
    dfrest=df.ix[set(df.index)-set(dfeb.index)-set(dfb.index)-set(dfl.index)-set(dfs.index)-set(dfd.index)]
    
    dfrest['eb']=1
    dfrest['b']=1
    dfrest['l']=1
    dfrest['s']=1
    dfrest['d']=1
    

    
    return pd.concat([dfeb,dfb,dfl,dfs,dfd,dfrest])


# In[66]:

df=pd.read_csv('C:\\Users\\hp\\Desktop\\temp.csv',encoding = "ISO-8859-1")
df.sample()


df=df.ix[df['Calories'] >100]
#col=df.columns[2:13]
#toRemove=df[col]


#removing Zero
'''
col=['Sodim'....]
temp=removeParticularElement(df,col)
df=temp
'''

#removing no entries
temp=removeMissingEntries(df,'food-item',indicationOfMissing='----')
df=temp
#df=df[df.index.isin(temp.index)]
print("after missing ",len(df))

#adding Disease value
temp=checkForDiabetes(df,'Total Carbs(g)',[30,60],modifyCol='Disease',inRangeValue='diabetes',outOfRangeValue='NA')
df=temp
#temp.sample()
print("after diabetes ",len(df))


#adding Allergies value
temp=checkForItems(df,'food-item',['Milk', 'Dairy', 'Ghee', 'Butter', 'Buttermilk','Yogurt', 'Cheese', 'Paneer','Icecream'],
                       modifyCol='Allergies',inRangeValue='Lactose',outOfRangeValue='NA')
df=temp
print("after allergies ",len(df))


#adding veg or non-veg to a food item
temp=checkForItems(df,'food-item',['Chicken', 'Pork','Shrimp', 'Prawn', 'Beef', 'Turkey', 'Bacon','Egg','chicken'],
                       modifyCol='veg/non veg',inRangeValue='non-veg',outOfRangeValue='veg')
df=temp
print("after veg and non-veg ",len(df))



#adding early-breakfast and all things
'''
earlybreakfast:
	water,

breakfast:
	Oatmeal, Yogurt, Wheat germ, Grapefruit, Bananas, Eggs,Almond butter,Watermelon
	, Flaxseed, Blueberries, Strawberries

Lunch:
	legume , vegetable ,bean salad ,avocado, pizza

snack:
	burger, idly, sandwich, pizza, mushroom, salami

dinner: 
	legume , vegetable ,bean salad ,avocado, pizza, icecream
    
'''
df['eb']=0
df['b']=0
df['l']=0
df['s']=0
df['d']=0



temp=giveEatingTime(df,
                    [' Water'],
                    ['Oatmeal','Yogurt','Wheat Germ', 'Bananas', 'Eggs', 'Strawberries', 'Watermelon','Blueberries','Flaxseed'],
                    ['Legume','Vegetable','Bean Salad', 'Avocado', 'Pizza'],
                    ['burger','idly','sandwich', 'pizza', 'mushroom', 'salami'],
                    ['Legume','Vegetable','Bean Salad', 'Avocado', 'Pizza','Icecream']
                   )
df=temp

print("after breakfast = , ",len(df))




df.sample()
#adding ethnicity



# In[67]:

import random
foo = ['North','South','East','West']


    
    
    
idx =df.index.tolist()

for i in idx:
    df.set_value(i, 'ethinicity', random.choice(foo))


# In[68]:

df.sample(3)


# In[69]:

df.to_csv(path_or_buf='temp.csv', sep=',')


# In[ ]:



