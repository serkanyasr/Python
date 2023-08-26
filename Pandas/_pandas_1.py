import numpy as np
import pandas as pd


# PANDAS SERİLERİ
numbers =[10,20,30,40,50]
letters = ["a","b","c",20]
dict= {"a":10,"b":20,"c":30}
pandas_series = pd.Series(numbers) # normal diziyi pandas serisine çevirir
pandas_series = pd.Series(letters) #  dizi ister ki string ya da int  bir değerler içersin
pandas_series = pd.Series(letters ,[0,1,2,3]) #  istersek index numaralarını bir liste olarak biz belirleyebiliriz
pandas_series = pd.Series(letters ,[0,1,2,3]) #  istersek index numaralarını bir liste olarak biz belirleyebiliriz
pandas_series = pd.Series(dict) # dict zaten key-value değerler oldğu için keyler index numarası olmaktadır
radom_value = np.random.randint(0,100,6)
pandas_series = pd.Series(radom_value) # numpy da ortak olarak kullanabilir
result =  pandas_series.ndim  # kaç boyutlu oldğunu gösterir
opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])

total = opel2018 + opel2019  # grandland ve mokka için NaN değeri çıkar çünkü  her iki dize de de en az bir tane var 
print(total) 
print(total["astra"])
----------------------------------------------------------------------------------------------------------------------------

#PANDAS DATAFRAME

df= pd.DataFrame()
s1 = pd.Series([1,2,3,4])
s2 = pd.Series([5,6,7,8])
data = dict(apples= s1,oranges = s2)

# df = pd.DataFrame(data)
print(df)

#FARKLI DOSYA TİPLERİNDEN VERİ OKUMA

df = pd.read_csv("dosya__adı.csv")
df = pd.read_sql_query("dosya__adı.sgl") 
----------------------------------------------------------------------------------------------------------------------------

#PANDAS DATAFRAMELER
from numpy.random import randn  #-1 le 1 arasında rasgele sayılar üretir

df = pd.DataFrame(randn(3,3),index=["A","B","C"] ,columns=["column1","column2","column3"]) # 3x3 lük indexleri ve coumn ları bellli yapı
result = df["column1"] 
result = df[["column1","column2"]]  #2 klonu da yazdırır

# loc["satır","sütun"] şeklinde kullanılır
result=df.loc["A"] # A satınının  sütunlarını yazdırır
result=df.loc[:,"column1"] # sadece column 1 yani sütunu yazdırır
result= df.iloc[1] #index ler içimn iloc kullamırzı
df["column4"]=pd.Series(randn(3),["A","B","C"]) #column4 ü oluşturduk
df["column5"]= df["column4"]+df["column2"]

result= df.drop("column5" ,axis=1 , inplace=True)  # column 5 i siler axis olmassa hata verirr 1 olası y eksenini 0 olmaası x eksenini temsil eder true olması kopyalamdadan direk orjial data ya yazar

print(result)
----------------------------------------------------------------------------------------------------------------------------
# DATAFRAME FİLTRELME

data = np.random.randint(0,100,75).reshape(15,5)

df = pd.DataFrame(data, columns=["column1","column2","column3","column4","column5"],)

result = df
result= df.columns # kolon bilgilerini getirirr

result=df.head() # ilk 5 satırı getirirC
result=df.head(10) # ilk 10 satırı getirir
result=df.tail() # son 5 satırı getirir
result= df["column1"].head()
result= df[["column1","column2"]].head() # seçilen kolonun  ilk 5 kydı getirilir 
result= df[5:15][["column1","column2"]].head() # 5 15 arasında il 5 kaydın kolon 1 ve 2 niin ilk 5 kaydı alır
result= df > 50 # 50 den büyükse true döndürür
result= df[df > 50] # 50 den büyük değerleri gösterir yoksa NaN yazar
result = df["column1"] >50  # sadece kolon 1 e bakar
result = df[(df["column1"] >50) & (df["column2"]<70)]  #  kolon 1 ve 2 için sağlayan değerler alınır yazdırılır
result= df.query("column1 >50 & column1<70") # yukarıda ki işlemi qery ile daha kolay yapabilmekteyiz
print(result)
----------------------------------------------------------------------------------------------------------------------------
#   DATAFRAME GROUPBY KULLNIMMI

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}
df = pd.DataFrame(personeller)
result= df

result= df["Maaş"].sum() # maaş katogorisinin toplmını alır
result= df.groupby("Departman").groups # grup hakkınada bilgi verir

semtler =df.groupby("Semt") # semt e göre gruplama yaprık ve fordöngüsü ile okuduk
# for name ,group in semtler:
#     # print(name)
#     # print(group)

result=  df.groupby("Semt").get_group("Kadıköy") # semti kadıköy olanları grupladık
result=  df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]) # np kullanrak tek satırda hepsini hesapladık

print(result)

----------------------------------------------------------------------------------------------------------------------------
# PANDAS BOZUK VERİ ANALİZİ

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data ,index=["a","c","e","f","h"], columns=["column1","column2","column3"])
newColumn = [np.nan,30,np.nan,40,np.nan,50,np.nan,70] # bozuk veri şeklinde bir kolon tanımladdık 
df =df.reindex(["a","b","c","d","e","f","g","h"])
df["column4"] =newColumn   # ekleme yaptık
result = df 
result= df.isnull() # değer olanlar false olmayanlar true döndürür
result= df.notnull() # sütekini tam tersi olur
result= df.isnull().sum() # NaN olan  kaç tane sayı var kolon olarak belirtir
result= df["column1"].isnull().sum() # kolon1 de kiler NaN ların sayısını belirtir
result= df.dropna() # satıda bozouk veri olmayan satırları getir
result= df.dropna( axis=1) # sütün da  bozouk veri olmayan satırları getir
result = df.dropna( how ="any") # satıda bozouk veri olmayan satırları getir
result = df.dropna( how ="all") # satırın  tamamı bozuk veri ise getirmez 
result= df.dropna(subset= ["column1","column2"], how = "all") # kolon 1 ve 2 de bozuk veri yi ara ve all ile yukrıda aynısı işlem 
result= df.dropna(thresh=2) # satırda 2 tane veri varsa o satırı silme
result= df.fillna(value ="no input") #NaN olan değerlere no input değerler atanır

print(result)
----------------------------------------------------------------------------------------------------------------------------


#   PANDAS İLE STRİNG FONKSİYONALRIN KULLANIMI

data = pd.read_csv(dosya_adı.csv)

data["Name"]= data["Name"].str.upper()  #str komutu il belirtilen komuta upper uyg ması yaparız

data  = data.Name.str.contains("Jordan") # Name kolonundan arama yapar ve jordan olanları true değeri döndürür
----------------------------------------------------------------------------------------------------------------------------

# PANDAS DATAFRAME METHODLARI
data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

result = df

result= df["Column1"].unique() # kolon 1 de ki tekrarlanmayan elemanları getirir
result= df["Column1"].nunique() # kolon 1 de ki tekrarlanmayan elemanların sayısını  getirir
result= df["Column1"].value_counts() # hangi elemanda kaç tane oldğunu gösterir
result= df["Column1"].apply("fonksiyon ismi") # apply ile içine verilen def fonk ı uygulanır
result= df.sort_values("Column2")  # kolon 2 de ki değeler sıralı olrak gelir
print(result)
----------------------------------------------------------------------------------------------------------------------------



