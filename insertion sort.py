#Sorting algorithm
S=[-39,-98,-20,1,6,8,4,2,7,-1000,998,56,78,42,6]
def Insertion_Sort(S):
        for i in range(1, len(S)):
                key=S[i]
                j=i-1
                while(j>=0 and S[j]>key):
                        S[j+1]=S[j]#sıralama başlıyor
                        j-=1#karşılaştırma yapabilmek için j her defasında bir azaltılıyor
                S[j+1]=key
print(S)
Insertion_Sort(S)
print(S)
