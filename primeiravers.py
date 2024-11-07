# Solicita ao usuário que digite 'F' ou 'M' e armazena a entrada na variável 's'
s = str(input('Digite F ou M: ')).strip().upper()[0]

# Enquanto a entrada não for 'M', 'm', 'F' ou 'f', continue solicitando uma entrada válida
while s not in 'MmFf':
    # Solicita ao usuário que digite novamente, informando que os dados são inválidos
    s = str(input('Dados inválidos, favor digite correto: ')).strip().upper()[0]

# Se a entrada for válida, exibe uma mensagem de sucesso
print('{} registrado com sucesso'.format(s))
