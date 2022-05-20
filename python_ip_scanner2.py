import subprocess
import re

first_ip = input("Entrez l'adresse de début = ")  # 192.168.1.1
last_ip = input("Entrez l'adresse de fin = ")
adresse_ip_connected = []

def get_Host(x):
    """
    Pour départager 3 premiers octets dans la variable Network
    Du dernier octet dans la variable first_Host (ou last_Host)
    """
    dot_Counter = 0
    pos_Counter = 0
    for i in x:
        if i == ".":
            dot_Counter += 1
        if dot_Counter == 3:
            return (x[0:pos_Counter + 1], x[pos_Counter + 1:])
            break
        pos_Counter += 1

Network, first_Host = get_Host(first_ip)
Network, last_Host = get_Host(last_ip)

print(Network)
print(first_Host)
print(last_Host)


empty_String = ""

counter = 0

for i in range(int(first_Host), int(last_Host) + 1):
    Process = subprocess.getoutput("ping -n 1 " + Network + str(i))  # Pour faire une seule fois appelle à ping
    empty_String += Process

    string_Needed = re.compile(r"TTL=")
    mo = string_Needed.search(empty_String)  # On recherche "TTL=" dans la recherche

    try:
        if mo.group() == "TTL=":  # Si "TTL=" est présent
            print("Host " + Network + str(i) + " répond")
            adresse_ip_connected.append(Network + str(i))
    except:  # Si "TTL=" n'y est pas
        print("Host " + Network + str(i) + " ne répond pas")

    empty_String = ""

print("Fini")
