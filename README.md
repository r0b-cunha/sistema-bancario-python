# 🏦 Sistema Bancário Orientado a Objetos em Python

Um sistema de linha de comando (CLI) que simula as operações de um banco, desenvolvido em Python. O projeto foi construído para aplicar e consolidar conceitos fundamentais de Engenharia de Software e Programação Orientada a Objetos (POO).

## 🛠️ Conceitos de Programação Aplicados

Este projeto demonstra o domínio de várias técnicas essenciais em Python:

- **Programação Orientada a Objetos (POO):** Criação de classes, instanciação de objetos e encapsulamento da lógica de negócios.
- **Herança:** A classe `ContaPoupanca` herda todos os atributos e métodos da classe base `ContaBancaria`, estendendo-a com comportamentos específicos (como o método de render juros).
- **Persistência de Dados:** Manipulação de ficheiros (`contas.txt`) para guardar o estado das contas e carregá-las automaticamente sempre que o programa é iniciado.
- **Tratamento de Erros e Exceções:** Uso de blocos `try / except` para capturar entradas inválidas do utilizador (como letras em campos de valores) e evitar que o programa vá abaixo.
- **Modularidade:** Divisão de responsabilidades entre funções de manipulação de ficheiros, lógica das classes e a interface de utilizador do menu.

## 🚀 Funcionalidades

- **Criação de Múltiplas Contas:** Suporte para abrir tanto Contas Correntes como Contas Poupança.
- **Submenus Dinâmicos:** Menu interativo que se adapta ao tipo de conta selecionada (a opção "Render Juros" só aparece para Contas Poupança).
- **Operações Bancárias Completas:** Consulta de saldo, depósitos e saques com validação de saldo suficiente.
- **Persistência Automática:** Os saldos e contas são atualizados num ficheiro local sempre que o utilizador sai do sistema.

## ⚙️ Como Executar o Projeto

1. Certifica-te de que tens o Python 3 instalado.
2. Clona este repositório para a tua máquina:
   ```bash
   git clone [https://github.com/TEU-UTILIZADOR/sistema-bancario-python.git](https://github.com/TEU-UTILIZADOR/sistema-bancario-python.git)
