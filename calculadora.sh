#!/bin/bash

echo "Iniciando Script"

echo "Diretorio atual: $PWD"

sudo apt update 
sudo apt install python3

python3 /home/guilherme/mod1/python/calculadora.py
