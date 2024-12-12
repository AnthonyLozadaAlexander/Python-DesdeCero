print("Bucle While")
print("------------")
PI = 3.1416

radio = int(input("Ingresar el radio: "))
while (radio <= 1):
  print("-------------------------------------")
  print("Debe ingresar un valor del radio > 1")
  radio = int(input("Ingrese un radio: "))

area = PI * radio ** 2
