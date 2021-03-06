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
    out = open('vhi_id_'+str(changeid(i))+'  time'+dt.strftime('%Y %m %d %H %M %S')+'.csv','wb') #we add time to csv file name and write down stuff in it
    out.write(vhi_url.read())
    out.close()
   
    return dt

def openframe(i, date):
    df = pd.read_csv(   'vhi_id_'+str(i)+'  time'+date.strftime('%Y %m %d %H %M %S')+'.csv',index_col=False, header=1)#we upload txt files data to excel
    df = df.rename(columns={'%Area_VHI_LESS_15': 'extrim', '%Area_VHI_LESS_35': 'temperate'}) #rename stuff for better purpose
    return df
    
def changeid(i): #change index in areas
    array = {1: 22, 2: 24, 3: 23, 4: 25, 5: 3, 6: 4, 7: 8, 8: 19, 9: 20, 10: 21, 11: 9,12: 26, 13: 10, 14: 11, 15: 12, 16: 13, 17: 14, 18: 15, 19: 16,20: 27, 21: 17, 22: 18, 23: 6, 24: 1, 25: 2, 26: 7, 27: 5}
    i=array[i]
    return i

def sort_by_year(df, year): #we sort,search some index and stuff
    t = df[df.year == year]
    print_VHI(t)
    
def max_VHI(df):
    t=df.ix[df['VHI'].idxmax()]
    print t
    
def min_VHI(df):
    t=df.ix[df['VHI'].idxmin()]
    print t

def sort_by_area_extr(df,a):
    t = df[df.extrim > a]
    print t.ix[:,[0,7]]

def sort_by_area_tmpr(df,a):
    t = df[df.temperate > a]
    print t.ix[:,[0,8]]
        

   
def print_VHI(df):
    print df.ix[:,[0,6]]
    
    

i = 1
while i < 2:  #we call out functions
    df=openframe(changeid(i), saving(i))
    sort_by_year(df,1985)
    max_VHI(df)
    min_VHI(df)
    sort_by_area_extr(df,20)
    sort_by_area_tmpr(df,35)
    i = i + 1
