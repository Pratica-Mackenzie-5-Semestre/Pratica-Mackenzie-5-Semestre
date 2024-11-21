# Projeto de Prática Profissional em ADS

Bem-vindo ao repositório do **Projeto de Prática Profissional em Análise e Desenvolvimento de Sistemas (ADS)**! Este projeto foi desenvolvido como parte do curso de ADS para aplicar conhecimentos teóricos em um ambiente prático.

## Links Importantes

1. [Github](https://github.com/Pratica-Mackenzie-5-Semestre) 
2. [Trello](https://trello.com/invite/b/66c12be448894743f8f64eb1/ATTI9e91298438963e1ea46b1813a7330893936BDA68/meu-quadro-do-trello)  

## Nome do Grupo: Planejamento Financeiro Sólido

## Integrantes do Projeto

1. **Alexia Gonçalves da Silva**  

2. **Bruno Brandão Costa Silva**  

3. **Gabriel de Almeida Moraes**  

4. **Leonardo Piauilino Marques**  

5. **Petrucio Alberto P. De Lima**  

  

## Professor Orientador

- **Pedro Henrique Cacique Braga**
- **Cristiano Moraes de Sousa**


## Objetivo do Projeto

Este projeto visa desenvolver um sistema de gerenciamento de finanças pessoais que permita aos usuários controlar suas receitas, despesas, investimentos e economias de forma eficiente. O sistema será construído utilizando a linguagem de programação Python e o banco de dados MySQL para armazenamento e manipulação dos dados financeiros dos usuários

## Tecnologias Utilizadas

- MySQL Connector/Python.
- Framework - Django
- Pandas e Matplotlib.
- bcrypt.
- Lucidchart.

## Projeto

![PSW7](https://github.com/user-attachments/assets/360ca99f-dfdb-47b3-a107-eb59f441f638)

# Configurações Iniciais

1. Crie o ambiente virtual:
   - Linux: `python3 -m venv venv`
   - Windows: `python -m venv venv`

2. Ative o ambiente virtual:
   - Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\Activate`

   > **Observação**: Se houver erro de permissão, execute o comando abaixo no PowerShell e tente novamente:
   > `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

3. Instale o Django e outras bibliotecas necessárias:
   ```bash
   pip install django
   pip install pillow

   
  
4. django-admin startproject core .
python3 manage.py startapp perfil
python3 manage.py startapp extrato

5. instale o GTK3 (necessário para integrações):

Acesse o link GTK3 para Windows e siga as instruções para instalação. https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases

6.  python3 manage.py startapp contas

7.  instale a biblioteca para converter HTML para PDF:
pip install weasyprint
