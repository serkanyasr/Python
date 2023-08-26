
from os import replace
from numpy.random.mtrand import randn
import numpy as np
import pandas as pd
from pandas.core import groupby
'''
pandas_series = pd.Series()
numbers = [10,20,30,40,50,70,80]
index= [1,2,3,5,6,7,8]
pandas_series = pd.Series(numbers)   # listeyi alır kendi incex atar
pandas_series = pd.Series(numbers,index)  #series in 2. değerine kendimiz index atayabilriz
pandas_series = pd.Series(numbers,["a","b","c","d","e","f","g"])  # kendimiz de index numaralarını liste olarak atayabilriz.

pandas_series= pd.Series([10,20,30,40], ["a","b","c","d"])

result= pandas_series.ndim        # boyutunu öğreniriz
result= pandas_series.dtype       # tipini öğreniriz
result= pandas_series.shape       # boyutunu öğreniz  matris olarak
result= pandas_series.sum()       # eleman toplamlarını öğreniirz
result= pandas_series.max()       # max elamanı yazar
result= pandas_series.min()       # min elemanı yazar
result=pandas_series+ pandas_series       #  2 seriyi toplar
result=pandas_series+ 50       # tüm elamnalanara 50 ekler
result=pandas_series >20       # 20 den büyük olanları true döndürür
result=pandas_series % 2 ==0       #  çift olanalrı true döndürür

#eğer 2 tane seriyi toplarsak karşılıklı değererleeri olmayanlara NaN döndrür







                  DATA FRAME
                  
2 PANDAS SERİSİNİN BİRLŞEMESİ İLE  OLUŞUR


s1= pd.Series([1,2,3,4])
s2= pd.Series([5,6,7,8])

data =dict(apples =s1,oranges=s2)
df= pd.DataFrame(data)

liste=[["serkan",100],["yasar",30],["yelda",70],["mercan",60]]
dict={"isim":["serkan","yasar","yelda","mercan"],"not":[100,30,70,60]}
dict_list=[
            {"name:":"serkan ","not:":"50"},    # isterse k böyle bir liste hazıralayıp df ye verirsek aynı sonuvu elde edeeriz
            {"name:":"yasar","not:":"60"},
            {"name:":"yelda","not:":"70"},
            {"name:":"mercan","not:":"80"},

        ]
df= pd.DataFrame(liste,columns=["isim","not"],index=[1,2,3,4],dtype=float) # data ,index , kolon sırasında belirtmez isen
df= pd.DataFrame(dict,index=[1,2,3,4])

df= pd.DataFrame(dict_list)
print(df)






data frame ile çalışma




from numpy.random import randint

df= pd.DataFrame(randn(3,3),index= ["A","B","C"],columns=["colum1","colum2","colum3"])

result=df
result=df["colum1"]   # kolokn 1 in değerlerini getirir  
result=df[["colum1","colum2"]]   # 1 den fazla kolon  için liste şeklinde gönderim yaparız

# loc["row","column"] => 1.satır seçimi 2. kolon seçimi hangisini boş bırakmak istiyorsan : koy ör satır için =>loc["row":,:] kolon için => loc [:,"kolon"]
result= df.loc["A"]   # belirlenen satırı alırız
result=df.iloc[1]  # index i belli olan df nin index numraları ile (1,2,3,4 etc) bilgi çekek istersek iloc kullanırız
result=df.loc[:,"colum1"] # sadece kolonu aldık
result= df.loc[:,"colum1":"colum3"]   # başlangıç ve bitişi belli edilen kolonu getir klon 1-2-3 gelir. başlangıç ve bitiş dahildir
result= df.loc[:,:"colum3"]   # başlangıçdan başla colum 3 e kadar git demeek
result=df.loc["A","colum3"]  # 1. girdi satırı 2.girdi sütün ddegerini verir

df["colum4"]=pd.Series(randn(3),["A","B","C",]) #kolon 4 ü tanımlayıp yine indexleerini vermemmiz gerekir.
df["colum5"]=  df["colum3"]+df["colum1"] 

df.drop("colum5",axis=1,inplace=True) # belirtilen koln silinir. kolon oldğunu belirmemiz için axis=1 satır oldğunu belrimemmzi için axis=0 girilmesi gerekir. inplace direk değişikliğ dosya ya yazar


data frame de filtreleme

data= np.random.randint(10,100,75).reshape(15,5)

df=pd.DataFrame(data ,columns=["column1","column2","column3","column4","column5",])


result= df
result=df.columns
result=df.head()
result=df.head(10)
result=df.tail()
result=df.tail(10)
result=df["column1"].head()  # kolon 1 den ilk 5 kaydı getir
result=df.column1.head()  # yukarıdajinin aynısı
result=df[["column1","column2","column3",]].head() 


result=df >50  # 50 den büüyk olanları true döndürürü
result=df[df>50]  # yukarıda k işlemi df ye verirsek true yerine değerlerini yazar

result= df[df["column1"]>50].column1

result= df[(df["column1"]>50) &(df["column2"]>50) ]["column1"]
result= df[(df["column1"]>50) &(df["column2"]>50) ][["column1","column2"]]
result= df[(df["column1"]>50) | (df["column2"]< 70 )]
result=df.query("column1>50 & column2>70")


print(result)

groupby

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df =pd.DataFrame(personeller)


result=df["Maaş"].sum()
result=df.groupby("Departman").groups   # hangi elamnlar gruplanmış onlar yazdırılır
result=df.groupby(["Departman","Semt"]).groups   # birden fazla elemanı grupndırmak için liste olarak girdi veririz

semtler = df.groupby("Semt")
# for name in semtler:
#     print(name)
result= df.groupby("Semt").get_group("Kadıköy") # semt grubundan sadece kadıköy oalanları al
result= df.groupby("Semt")["Maaş"].sum() # semt grubunda oalnalrı al ve maaşlarını toplamını  hesapla
result= df.groupby("Semt").get_group("Kadıköy")["Maaş"].sum() # semt grubundan sadece kadıköy oalanları al ve maaşlarını topla
result= df.groupby("Semt")["Çalışan"].count() #  semt e göre gupla ve kaç kişi hangi semt de çalışıyor
result= df.groupby("Departman").agg(np.mean )  # agg metodu ile fonksiyonları kullanabilirriz numpy yardımı ile ortalama aldık
result= df.groupby("Departman")["Maaş"].agg([np.mean,np.sum,np.max,np.min])  # agg ile tek sefer de aynı işlmeleri yazdırabilriz
result= df.groupby("Departman")["Maaş"].agg([np.mean,np.sum,np.max,np.min]).loc["Muhasebe"]  # agg ile tek sefer de aynı işlmeleri yazdırabilriz ve bunu loc yarıdımı ile 1 eleman için heaplatabilriz

print(result)

        PANDAS KAYIP VE BOZUK VERİ İLE ÇALIŞMA


data = np.random.randint(10,100,15).reshape(5,3)
df=pd.DataFrame(data,index=["a","c","e","f","h"],columns=["column1","column2","column3"])
df=df.reindex(["a","b","c","d","e","f","g","h"])

resutl=df
resutl=df.drop("column1",axis=1) # drop ile kolon silme yapabilriz 2.parametre olarak axis 1 kolon 0 değeri satıra denk gelir
resutl=df.drop("a",axis=0 ) # drop ile kolon silme yapabilriz 2.parametre olarak axis 1 kolon 0 değeri satıra denk gelir
resutl=df.isnull()  # NaN olanlar True değeri döndürür
resutl=df.notnull()  # NaN olanlar False değeri döndürür
resutl=df.isnull().sum()  # NaN kaç tane var




print(resutl)'''