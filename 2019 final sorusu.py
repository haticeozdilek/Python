for n in range(1,10,2):#1'den başlayarak 10'a kadar 2'şer artacak
    for p in range(2,10,2):#2'den başlayarak 10'a kadar 2'şer artacak
        if(p**2<n):
            print(p)
            break
    else:
        print(n)
else:
    print(n-p)