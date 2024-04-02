dig = 0
num = int(input("digite um número: "))
numoriginal = num
print (num)
while (num !=0 ):
    dig = dig*10 + num%10
    if(dig==0):
        dig = dig*10 + num%100
        num = num//100
    else:
        num = num//10
print(dig)
if(dig==numoriginal): 
    print("O número é palindromo")
else:
    print("O numero não é palindromo.")