import random, string, os, time
from pathlib import Path

class Cores:

    cor_azul = '\033[1;34m'
    cor_magenta = '\033[1;35m'

def menu():

    menux = """
    
   ####################
   # GERADOR DE SENHA #
   ####################
   """

    os.system('clear')
    print(Cores.cor_azul + menux)
    time.sleep(1)


menu()

comprimento = int(input('Informe o comprimento da senha: '))

gerar_senha = ''.join(random.sample(string.ascii_uppercase + string.digits + string.ascii_lowercase, comprimento)) # Letras maiúsculas + números + letras minúsculas, comprimento da senha

print()

senha = 'Senha: ' + gerar_senha

arquivo = open('senha.txt', 'w+') # Cria um arquivo chamado senha.txt
arquivo.write(senha) # Escreve a senha no arquivo txt

diretorio = Path().absolute()

# Informa ao usuário que a senha foi gerada e exibe o diretório do arquivo
print(f'''
##########################
Um arquivo txt com a senha 
foi gerado...

Diretório: {diretorio}
##########################
''')
