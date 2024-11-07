# Solicita ao usuário que digite 'F' ou 'M' e armazena a entrada na variável 's'
s = input('Digite F ou M: ').strip().upper()[0]

# Conjunto de entradas válidas
valid_inputs = {'F', 'M'}

# Enquanto a entrada não for válida, continue solicitando uma entrada válida
while s not in valid_inputs:
    # Solicita ao usuário que digite novamente, informando que os dados são inválidos
    s = input('Dados inválidos. Favor digitar "F" para feminino ou "M" para masculino: ').strip().upper()[0]

# Se a entrada for válida, exibe uma mensagem de sucesso
print('{} registrado com sucesso'.format(s))
