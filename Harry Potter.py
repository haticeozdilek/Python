title=int(input("How many words are in the title of the letter ?"))
x=title//10
if (x==0 & x>=10):
    print("The letter was delivered")
else:
    value=title % 10
    sum=x+value
    multiplying=x*value
if(title==(sum+multiplying)):
    print("Harry Potter received the letter")
else:
    print("The letter was destroyed")

