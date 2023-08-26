import numpy as np

# NUMPY ARRAY
np_array = np.array([1,2,3,4,5,6,7,8,9]) # tek boyutlu bir dizi 
py_multi =[[1,2,3],[4,5,6],[7,8,9]]
np_multi  =np_array.reshape(3,3) # olan diziyi 3 e 3 matrise çevirir
np_array.shape # boyutu söyler


#NUMPY DİZİLERDE ÇALIŞMA


result = np.array([1,2,3,4,5])
result=np.arange(1,10)# 1 den 10 dağil değil e kadar numpy dizisi oluşturur
result=np.arange(1,100,3)# 1 den 100 dağil değil e kadar numpy dizisi oluşturur ama 3 er 3 er artarak
result= np.zeros(10) # 10 tane sıfırdan oluşan dizi oluşturur
result= np.ones(10) # 10 tane bir den  oluşan dizi oluşturur
result=np.linspace(0,100,5)# 0 la 100 ü 5 parçaya böler
result=np.random.randint(0,10)# 0 la 10 arasında int bir  tane değer atar. 3.değer kaç tane üretilmesini temsil eder
result= np.random.rand(5) # 0 la 1 arasında 5 değer atar
np_array =np.arange(50)
result= np_array.reshape(5,10) # 5x10 luk maatris yapısını alır 2 boyutlu olur
result= result.sum(axis=1) # satırlrın toplamını verir
result= result.sum(axis=0) # sütunaları toplamını verir
numbers= np.random.randint(1,100,10)
result= numbers.argmax() # dizi de ki en yüksek değerin kaçıncı index de bulunduğunu gösterir
result= numbers.argmin() # dizi de ki en düşük değerin kaçıncı index de bulunduğunu gösterir

#NUMPY DİZİLERİN İNDEXLENMESİ

numbers = np.array([5,10,15,20,25,50,75])

result=numbers[5] # dizinin 5.i ndex ini atar 
result=numbers[-1] # dizinin en son  index ini atar 
result=numbers[0:3] # dizinin 0 dan 3e kadar olan sayıalrı atar 
result=numbers[:3] # dizinin 0 dan 3e kadar olan sayıalrı atar 
result=numbers[3:] # dizinin 3 den sona kadar olan sayıalrı atar 
result=numbers[::] # dizinin tüm sayıalrı atar 
numbers2 = np.array([[5,10,15],[20,25,50],[75,80,85]]) # 3x3 matris yapısını alır

result= numbers2[0] # [5,10,15 ] i alır
result= numbers2[0,2] # 15 i alır
result= numbers2[:,2] # 15,50,85 değerlerini alır : tüm diziyi seçer ve onların 2 .index ini alır   
result= numbers2[:,0:2] #  : tüm diziyi seçer ve onların 0 -2 index dedkini yazdırır

#   NUMPY DİZİ OPERASYONLARI

numbers1= np.random.randint(1,100,6)
numbers2= np.random.randint(1,100,6)

result = numbers1+numbers2
result= numbers1 +10 # her değere 10 ekler
result= np.sin(numbers1) # her index in sin i alınır
result= np.sqrt(numbers1) # karekökünü alır 

mnumbers1=numbers1.reshape(2,3)
mnumbers2= numbers2.reshape(2,3)

result= np.vstack((mnumbers1,mnumbers2)) # 2x3 olan 2 matrisi alt alta birleştirir ve 4x3 lu matris elde edilir
result= np.hstack((mnumbers1,mnumbers2)) # 2x3 olan 2 matrisi yan yanabirleştirir ve 2x6 lu matris elde edilir
result= numbers1 >=5  # dizi de ki değerleri gezer ve 5 den büyük se true değerini döndürür
