sum,sumofSquares=0,0
for i in range(1,101):
    sum+=i
    sumofSquares+=i**2
    print(sum**2-sumofSquares)