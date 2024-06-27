
CONSTANTE_BONUS = 1000

# 1) Solicite ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")

# 2) Solicite ao usuário que digite o valor do seu salário
# Converta a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite seu salário: "))

# 3) Solicite ao usuário que digite o valor do bônus recebido 
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o valor do bônus: "))

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario*bonus_usuario

# 5) Imprima a mensagem persolazida incluindo o nome do usuário,e o valor do bônus
print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")
