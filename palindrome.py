#Tersten okunduğunda da aynı olan kelimelere palindrom denir. Palindrom, tersten okunuşu da aynı olan cümle,
# sözcük ve sayılara denilmektedir.
def reverse(a):
    return a[::-1]#listeyi tersine çeviriyor
def isPalindrome(a):
    if(a == reverse(a)):
        return True
    return False
print(isPalindrome("rever"))
print(isPalindrome("algorithm"))
print(isPalindrome("ahaha"))