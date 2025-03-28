def change():
    expense = 23.75
    money = 100
    gasto = float(input("Ingrese gasto: \n"))
    print(gasto)

    recibo = float(input("Dinero recibido \n"))
    print(recibo)

    pesos = recibo-gasto 
    centavos = (float(pesos)-int(pesos))*100

    print("\nVuelto\n")
    print("Pesos:\n")
    print(pesos)
    print("Centavos:\n")
    print(centavos)
