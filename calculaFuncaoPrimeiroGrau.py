# Aluna: Cássia Oliveira dos Santos;
# # IFPA - Campus Santarém; Turma: Info20
# Professor: Kleberson Serique do Amaral Serique.

#Informações ao usuário sobre a finalidade do programa:
print("""Caro usuário, este programa calcula a função do primeiro grau!!! Veja:

f(x) = ax + b, onde a e b pertencem ao conjunti dos números Reais e a é diferente de 0.
a = coeficiente;
b = termo constante;

Para calcular, precisarei de dois valores da função - primeiramente o de a depois o de b.
""")

# 1º crio variáveis que apontarão para o local na memória dos valores inseridos pelo usuário:
value_A = float (input("Insira o valor de a: "))#recebe entrada e converte para float;
#O valor de a não pode ser igual a 0:
while value_A == 0:
	value_A = float(input("Valor é inválido para a! Por favor, insira um novo!\nInsira o valor de a: "))#imprime e espera nova entrada toda vez que o usuário digitar 0 para a.

value_B = float (input("Insira o valor de b: "))#recebe entrada e converte para float;

if value_B == 0:
	print("\nO resultado da sua função é 0.")
else:
    print("\nO resultado da sua função é: ", (value_B * ( -1))/value_A, ".")

print("""
Obrigada por utilizar o programa!!! :)""")