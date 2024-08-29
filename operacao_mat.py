#vamos solicitar como entrada dois numero e depois realizar uma operação simples entre eles.


num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite segundo número: "))

operacao =  input("escolha a operação (+, - ,* , /): ")

if operacao == "+":
    result = num1 + num2
    print(f"o resultado da adição é: {result}")
elif operacao == "-":
    result = abs(num1 - num2)
    print(f"o resultado da subtraçao é: {result}")
elif operacao == "*":
    result = num1 * num2
    print(f"o resultado da multiplicação é: {result}")
elif operacao == "/":
    if num2 != 0: #verifica se o divisor nao é zero
        result = num1 + num2
        print(f"o resultado da divisãp é: {result}")
    else:
        print("error: divisão por zero não pe permitida.")
else:
    print("operação invalida.")
