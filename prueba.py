
def invertir(n,x= 0):
    if n ==0:
        return x
    else:
        return invertir(n= n//10 , x= x*10 +n%10)
    
print(invertir(123))
    