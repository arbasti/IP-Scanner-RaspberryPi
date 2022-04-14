"""
MVP :
Récupérer les adresses IP distribué avec un code en python

Description :
La méthode est par Brutforce
Le problème étant que cette méthode est très longue en attente

Sources :
- https://tutoriels.pecaudchristopher.com/tutoriels_windows/espace_python/Tutoriel_Creation_Scanner_IP_Python.php#Intro
- https://docs.python.org/3/library/socket.html
"""

import socket  # voir source

# On ping les adresses IP disponibles
for ping in range(1,254):  # 0 et 255 étant le routeur et le broadcast ne sont pas compris
    address = "192.168.1." + str(ping)  # On écrit toutes les adresses IP de 1 à 254
    socket.setdefaulttimeout(1)

    try:
        # On ping les adresses IP une par une et on renvoie un triple dans les variables
        hostname, alias, addresslist = socket.gethostbyaddr(address)
    
    # Si on ne reçoit rien en retour après le ping, on implémente None au différente variable
    except socket.herror:
        hostname = None
        alias = None
        addresslist = address

    print(addresslist, '=>', hostname)  # On print le résultat de notre recherche
