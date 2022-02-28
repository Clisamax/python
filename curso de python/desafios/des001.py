import socket as s

# Host que deseja descobrir o Ip #
h = input('Digite o nome do site : ')
host = h

# Capturar o Ip do Host desejado #
Ip = s.gethostbyname(host)

# Mostra resultados #
print('O Ip do Host " ' + host + ' " é: ' + Ip)