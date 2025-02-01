📌 Calculadora Python 🧮

Este projeto é uma calculadora simples desenvolvida em Python, capaz de realizar operações matemáticas básicas. Ele pode ser executado diretamente pelo Python ou por meio de um script shell para facilitar sua utilização.

📂 Estrutura do Projeto

calculadora.py: Script principal da calculadora.

calculadora.sh: Script shell para executar a calculadora automaticamente.


🚀 Como Executar

🔹 Método 1: Executando o Script Python Diretamente

Se você tem o Python instalado, pode executar o script diretamente no terminal:

python3 calculadora.py

Isso iniciará a calculadora, permitindo que você insira dois números e escolha uma operação matemática.

🔹 Método 2: Usando o Script Shell (calculadora.sh)

O script shell (calculadora.sh) serve para facilitar a execução do código Python sem precisar digitá-lo manualmente. Siga os passos abaixo para executá-lo:

Dê permissão de execução ao arquivo:

chmod +x calculadora.sh

Execute o script:

./calculadora.sh

Isso iniciará automaticamente o script Python da calculadora.

📝 Explicação do Código

🔹 calculadora.py

O script inicia um loop infinito que permite ao usuário realizar várias operações matemáticas sem precisar reiniciar o programa. Ele segue os seguintes passos:

Solicita ao usuário dois números;

Pergunta qual operação matemática deseja realizar;

Verifica a operação escolhida e executa o cálculo correspondente:

- Soma (SOMA ou +)

- Subtração (SUBTRACAO ou -)

- Multiplicação (MULTIPLICACAO, * ou X)

- Divisão (DIVISAO ou /)

- Exibe o resultado da operação.

- Pergunta se o usuário deseja realizar outro cálculo.

Se o usuário responder "NÃO" ou "N", o programa encerra.

Exemplo de entrada e saída:

Digite o primeiro número: 10
Digite o segundo número: 5
Qual operação matemática deseja fazer? +
15.0
Deseja fazer outro cálculo? (Sim/Não): Não
Encerrando o programa...

🔹 calculadora.sh

O script shell simplesmente executa o código Python automaticamente. Seu conteúdo pode ser algo como:

#!/bin/bash
python3 calculadora.py

Ele garante que o script Python seja iniciado sem precisar digitá-lo manualmente no terminal.

📥 Download e como Usá-lo :

Clone este repositório:

git clone [https://github.com/oGuiCorreia/Ebac-Analise_de_Dados]

Acesse a pasta do projeto:

cd Ebac-Analise_de_Dados

Execute a calculadora pelo Python ou pelo script shell.

📌 Observação

O código foi escrito para funcionar em qualquer sistema operacional que suporte Python.

Certifique-se de que tem o Python instalado (versão 3 ou superior).

Agora você pode utilizar sua calculadora! 🚀

