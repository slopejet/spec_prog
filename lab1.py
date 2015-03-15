import  urllib2
import pandas as pd
import datetime 


def saving(i):
    if i<10: #download data
        url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R0"+str(i)+".txt"
    else :
        url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+str(i)+".txt"
    vhi_url = urllib2.urlopen(url)
    dt = datetime.datetime.now()
    out = open('VHI'+str(changeid(i))+'.csv','wb') # out = open('vhi_id_'+str(changeid(i))+'  time'+dt.strftime('%Y %m %d %H %M %S')+'.csv','wb')
    out.write(vhi_url.read())
    out.close()
    return dt

def openframe(i, date):
    df = pd.read_csv(   'VHI'+str(i)+'.csv',index_col=False, header=1) #df = pd.read_csv(   'vhi_id_'+str(i)+'  time'+date.strftime('%Y %m %d %H %M %S')+'.csv',index_col=False, header=1)
    df = df.rename(columns={'%Area_VHI_LESS_15': 'extrim', '%Area_VHI_LESS_35': 'temperate'})
    return df
    
def changeid(i): #change index in areas
    mas = {1: 22, 2: 24, 3: 23, 4: 25, 5: 3, 6: 4, 7: 8, 8: 19, 9: 20, 10: 21, 11: 9,12: 26, 13: 10, 14: 11, 15: 12, 16: 13, 17: 14, 18: 15, 19: 16,20: 27, 21: 17, 22: 18, 23: 6, 24: 1, 25: 2, 26: 7, 27: 5}
    i=mas[i]
    return i

def maxVHI(df):
    t=df.ix[df['VHI'].idxmax()]
    print t
    
def minVHI(df):
    t=df.ix[df['VHI'].idxmin()]
    print t
    
def connect_path(path, name): 
    res = os.path.join(path, name)
    return res

def SortedYear(df, year): #we sort,search some index and stuff
    t = df[df.year == year]
    printVHI(t)
   
def SortedAreaExtr(df, a):
    t = df[df.extrim > a]
    print t.ix[:,[0,7]]
    
def SortedAreaTmpr(df, a):
    t = df[df.temperate > a]
    print t.ix[:,[0,8]]
   
def printVHI(df):
    print df.ix[:,[0,6]]
    
    

i = 1
while i < 27: #we call out functions
    df=openframe(changeid(i), saving(i))
    SortedYear(df, 1985)
    maxVHI(df)
    minVHI(df)
    SortedAreaExtr(df, 20)
    SortedAreaTmpr(df, 35)
    i = i + 1

