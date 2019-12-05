# -*- coding: utf-8 -*-

n=input("bir sayi girin :")#6 için
t=1
for i in range(2,5):#2,3,4
   if(int(n)%i==0):
      t*=i
   if(t==int(n)):
    print(t)
else: #for döngüsünden çıkıp 6-6 yazacak
    print(int(n)-t)