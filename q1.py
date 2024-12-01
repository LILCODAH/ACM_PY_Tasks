m=int(input("enter a number: "))
n=int(input("enter an another number: "))
suma=0
for num in range(m,n+1):
    suma+=num
    
print(f"The sum of numbers between {m} and {n} is: {suma}")    