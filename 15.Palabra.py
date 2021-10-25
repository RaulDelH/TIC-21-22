def palabra2 ():
    nombre = raw_input ("NOMBRE: ")
    apellido = raw_input ("APELLIDO: ")
    print ("BUENOS DIAS MI ESTIMADO, " + nombre + " " + apellido)
    print ("tu sensual nombre empieza por la letra " + nombre[0])
    print ("Voy a deletrear tu sensual nombre")
    for cont in range (0, 20):
        print (nombre[cont])
palabra2 ()
