num1 = input ("Digite um numero: ")
num2 = input ("Digite outro numero: ")
convert_num1 = int(num1)
convert_num2 = int(num2)
if convert_num1 > convert_num2:
    print ("O primeiro numero digitado é o maior")
elif convert_num1 < convert_num2:
    print ("O segundo numero digitado é o maior")
else:
    print ("Os numeros sao iguais")