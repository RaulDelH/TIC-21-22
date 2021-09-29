def tabla2():
    print("*************************")
    print("* Calculadora de tablas *")
    print("*************************")
    numero=input("De que numero deseas saber la tabla?: ")
    for cont in range(0,11):
        print(str(numero)+" x "+str(cont)+" = "+str(numero*cont))
    print("FIN SERAFIN")
tabla2()
