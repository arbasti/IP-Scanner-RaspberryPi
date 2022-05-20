# IP-Scanner-RaspberryPi

## Objectif :
- Détecter les utilisateurs connecté à un wifi depuis un Raspberry Pi 3
- Ajouter dans une base de donnée :
  - Les différents utilisateurs
  - Leurs nombres de connections
  - Leurs heures de connections

## Module :
```python
import subprocess
import re
```

## Base de Donnée :
Les fichiers de la base de donnée seront stocker sous un **.json**

## Logiciel :
- Angry IP Scanner

## MVP :
- Afficher la liste des utilisateurs connectés au réseau
- Ajouter la le programme dans un Raspberry pi puis l'automatiser avec des timers

![Image Raspberry Pi 3](https://m.media-amazon.com/images/I/91zSu44+34L._AC_SL1500_.jpg)
