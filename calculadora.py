#calculadora.py
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b

if __name__== "__main__":
    #Referencias
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    resultado = sumar(num1, num2)
    print(f"El resultado de la suma es: {resultado}")
    print(f"El resultado de la resta es: {restar(num1, num2)}")