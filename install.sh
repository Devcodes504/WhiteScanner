#!/bin/bash
echo "[+] Instalando WhiteScanner..."
pkg install python nmap -y
pip install colorama requests python-nmap
chmod +x run.sh
echo "[+] Ejecuta con: bash run.sh"
