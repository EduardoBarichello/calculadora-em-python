import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Erro! Raiz quadrada de número negativo."
    return math.sqrt(x)

def logarithm(x, base=math.e):
    if x <= 0:
        return "Erro! Logaritmo de número não positivo."
    return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Erro! Fatorial de número negativo."
    return math.factorial(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def main():
    print("Calculadora Científica")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Logaritmo")
    print("8. Fatorial")
    print("9. Seno")
    print("10. Cosseno")
    print("11. Tangente")
    
    while True:
        choice = input("Digite sua escolha (1/2/3/.../11): ")

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if choice == '1':
                print(f"Resultado: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Resultado: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Resultado: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Resultado: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"Resultado: {num1} ** {num2} = {power(num1, num2)}")

        elif choice == '6':
            num = float(input("Digite o número: "))
            print(f"Resultado: √{num} = {square_root(num)}")

        elif choice == '7':
            num = float(input("Digite o número: "))
            base = input("Digite a base (pressione Enter para base e): ")
            if base == '':
                print(f"Resultado: log({num}) = {logarithm(num)}")
            else:
                base = float(base)
                print(f"Resultado: log({num}, {base}) = {logarithm(num, base)}")

        elif choice == '8':
            num = int(input("Digite o número: "))
            print(f"Resultado: {num}! = {factorial(num)}")

        elif choice == '9':
            angle = float(input("Digite o ângulo em graus: "))
            print(f"Resultado: sin({angle}) = {sine(angle)}")

        elif choice == '10':
            angle = float(input("Digite o ângulo em graus: "))
            print(f"Resultado: cos({angle}) = {cosine(angle)}")

        elif choice == '11':
            angle = float(input("Digite o ângulo em graus: "))
            print(f"Resultado: tan({angle}) = {tangent(angle)}")

        else:
            print("Opção inválida, tente novamente.")
        
        next_calculation = input("Deseja fazer outra operação? (sim/não): ")
        if next_calculation.lower() != 'sim':
            break

if __name__ == "__main__":
    main()
