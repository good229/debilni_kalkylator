# ДЕБИЛЬНИЙ КАЛЬКУЛЯТОР

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

operation = input("Что сделать? (+, -, /, *): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "/":
    result = a / b
elif operation == "*":
    result = a * b

print(f"Результат: {result}")
