#Bir öğrenci sınava, sınavdan belli bir süre önce çalışmaya başlarsa yeterli olacağını düşünüyor.Bu süreyi saniye
#cinsinden hesaplarken bulacağı sayının onlar basamağı birler basamağının kuvveti kadar, birler basamağı da yüzler
#basamağının kuvvetiyle çarpıldığında sayıya eşit olmasını istiyor.Sınava en az kaç saniye kala çalışması gerektiğini
#bulan python programı

for i in range(1000,10000):
    x,y,z,k,number=0,0,0,0,0
    x=i//1000       #Pythonda "//" ifadesi bölme işleminde tam değer almayı sağlıyor
    y=(i-x*1000)//100
    z=(i-x*1000-y*100)//10
    k=(i-x*1000-y*100-z*10)
    number=(z**k)*(x**y)
    if(number == i):
        print("work for at least %d seconds"%i)
    else:
        continue
