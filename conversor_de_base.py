baseinver2 = 2
base2 = 0
base10 = int(input("escreva um número: "))
while(base10!=0):
    baseinver2 = baseinver2*10 + base10%2
    base10 = base10//2
    print(baseinver2)
while(baseinver2!=2):
    base2 = base2*10 + baseinver2%10
    baseinver2 = baseinver2//10
    print(base2)

print("O número em binario é: ", base2)