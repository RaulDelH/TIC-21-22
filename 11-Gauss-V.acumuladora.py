def Gauss2():
    n=input("Hasta donde cuento: ")
    acum=0
    for cont in range (1,n+1):
        acum=acum+cont
        print(str(cont)+" acum= "+str(acum))
Gauss2()
