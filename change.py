def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int(round((vuelto-pesos)*100))
    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")
	
