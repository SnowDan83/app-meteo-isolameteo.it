#!/bin/bash

# Abilita l'accesso al server X per l'utente corrente (per la GUI)
xhost +local:$USER > /dev/null

# Lancia lo script Python
# Nota: Se il tuo sistema usa "python3", cambia "python" con "python3" qui sotto
python "/home/danyslipknot/My_Software/App_Meteo/START.pyw"