import matplotlib.pyplot as plt
import numpy as np

x= [1,2,3,4]
y = [2,4,9,16]
plt.plot(x,y,color="red",linewidth="5") # çizginin kalınlığını ve rengini belirler
plt.axis([0,6,0,20])  # x ekseni 0- 6 arasın da y ekseni 0,20 arasıda olcak
plt.title("grafik başlığı") # grafiğin adı başlığı dır
plt.xlabel("x ekseni ismi")
plt.ylabel("y ekseni ismi")
# ------------------------------------------------------------------------------------------------------------
x = np.linspace(0,2,100)  # 0 la 2 yi 100 yaprcay böldük
plt.plot(x, x ,label = "linear")  # bu 3 aşamada fonk belirlioyruz
plt.plot(x, x**2 ,label = "quadratic")
plt.plot(x, x**3 ,label = "cubic")

plt.xlabel("x ekseni") 
plt.ylabel("y ekseni")
plt.legend() #legend ile belirtile label lar grafiğn kenarında gözükmetedir
plt.show()
#------------------------------------------------------------------------------------------------------------


x = np.linspace(0,2,100) 
fig,axs = plt.subplots(2) # alt alta  2 tane grafik oluşturmak için kullanuuıırız 

axs[0].plot(x,x) # 1 .grafik
axs[0].set_title("linear")
axs[1].plot(x**2) #2. grafik
axs[1].set_title("quadratic")


plt.show()
#------------------------------------------------------------------------------------------------------------

x = np.linspace(0,2,100) 
fig,axs = plt.subplots(2,2)
fig.suptitle("grafik başlığı")
axs[0,0].plot(x,x) # 1 .grafik 
axs[0,1].plot(x**2) #2. grafik    # alt alta ve üst üste grafikler çizdik
axs[1,0].plot(x**3) #3. grafik
axs[1,1].plot(x**4) #4. grafik

plt.show()
#------------------------------------------------------------------------------------------------------------


# MATPLOTLİB İLE FİGÜRE OLUŞTURMA

x =  np.linspace(-10,9,20)
y = x**3
z = x**2

figure =plt.figure() # fıguuru oluşturduk 
axes = figure.add_axes([0.1,0.1,0.8,0.8])  # eksenlerin sıraile sol  sağdan yüzde kaç boşluk olsun ve 0.9 ise %90 ekrana sığsın
axes.plot(x,y,"b") # çizdirme işlemi 
axes.set_xlabel("X Axis") # x ekseni ismini beilrledik
axes.set_ylabel("Y Axis") # y ekseni ni belirledik
axes.set_title("grafik başlığı") 
# grafiğin içinde olan grafik
axes2 = figure.add_axes([0.15,0.6,0.2,0.2])  # eksenlerin sıraile sol  sağdan yüzde kaç boşluk olsun ve 0.9 ise %90 ekrana sığsın
axes2.plot(x,z,"r") 
axes2.set_xlabel("X Axis")
axes2.set_ylabel("Y Axis")
axes2.set_title("axes2 grafik başlığı")
#------------------------------------------------------------------------------------------------------------
figure =plt.figure() # fıguuru oluşturduk 
axes = figure.add_axes([0,0,1,1]) # sayfanın tamamını kaplayan bir figür oluşturduk 
axes.plot(x,z, label = "square") # 1. grafikh
axes.plot(x,y ,label = "cube ")  #2.grafik
axes.legend()

#------------------------------------------------------------------------------------------------------------
#yukarı da oluşturulan figürü istersen subplot ile oluşturabliriz
fig,axes = plt.subplots(nrows=2,ncols=1 , figsize= (8,8)) # 2 1 olması 2 figire olcak alt alta
axes[0].plot(x,y)
axes[0].set_title("1.grafik başlığı")
axes[1].plot(x,z)
axes[1].set_title("2.grafik başlığı")

fig.savefig("figüre.png")  # figürü kayıt eder 
plt.show()
#------------------------------------------------------------------------------------------------------------



# matplotlib grafik türleri
# Stack plot    # hacimsel olarak çizilen grafik
yil = [2011,2012,2013,2014,2015,]

oyunucu1 = [8,10,12,7,9]
oyunucu2 = [3,40,15,6,45]
oyunucu3 = [4,30,32,3,34]


plt.plot([],[],color="y", label = "oyuncu1")   # boş figürleri oluşturduk
plt.plot([],[],color="r", label = "oyuncu2")
plt.plot([],[],color="b", label = "oyuncu3")
plt.stackplot(yil,oyunucu1,oyunucu2,oyunucu3, colors=["y","r","b"])   
plt.title("yıllara göre atılan goller")
plt.xlabel("yil")
plt.ylabel("gol sayısı")
plt.legend()
plt.show()
#------------------------------------------------------------------------------------------------------------

# pie grafiği

goal_type = "penaltı","kaleye atılan şut","serbest vuruş"

goals = [12,15,17]
colors = ["y","r","b"]


plt.pie(goals,labels= goal_type ,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%") # dairesel olarak figüre oluşturduk shadow glge verir explode dilimler arasında ki mesafeyi gösterir autopct dilimlerin yüzdelerini gösterir


plt.show()
#------------------------------------------------------------------------------------------------------------



# bar grafiği
plt.bar([2,4,5,4,8],[50,20,80,100,15] , label = "BMW" ,width=.5)
plt.bar([1,2,4,5,6],[40,30,60,70,45] , label = "Audi" , width=.5)
plt.legend()
plt.xlabel("gün")
plt.ylabel("Mesafe")
plt.title("araç bilgileri")
plt.show()

#------------------------------------------------------------------------------------------------------------

