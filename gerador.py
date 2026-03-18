import random
import string

print("Gerador de Senhas Seguras")

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ''.join(random.choice(caracteres) for i in range(tamanho))

print("Senha gerada:", senha)
